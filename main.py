from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)


class IssueModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    issue = db.Column(db.String(100), nullable=False)
    type = db.Column(db.String(10), nullable=False)

    def __refr__(self):
        return f"Issue(Name={name}, Issue={issue}, Type={type})"


issue_args = reqparse.RequestParser()
issue_args.add_argument('name', type=str, help='Enter Name', required=True)
issue_args.add_argument('issue', type=str, help='Enter the issue', required=True)
issue_args.add_argument('type', type=str, help='Enter type of issue', required=True)

issue_update_args = reqparse.RequestParser()
issue_update_args.add_argument('name', type=str, help='Enter Name')
issue_update_args.add_argument('issue', type=str, help='Enter the issue')
issue_update_args.add_argument('type', type=str, help='Enter type of issue')


resources_fields = {
    'id': fields.Integer,
    'name': fields.String,
    'issue': fields.String,
    'type': fields.String
}


class IssueRead(Resource):
    @marshal_with(resources_fields)
    def get(self, user_id):
        result = IssueModel.query.filter_by(id=user_id).first()
        if not result:
            abort(404, message='No Issue raised for the given ID')
        return result

    @marshal_with(resources_fields)
    def put(self, user_id):
        args = issue_args.parse_args()
        result = IssueModel.query.filter_by(id=user_id).first()
        if result:
            abort(409, message= 'Already an issue is raised under given ID. Kindly update the issue')

        read = IssueModel(id=user_id, name=args['name'], issue=args['issue'], type=args['type'])
        db.session.add(read)
        db.session.commit()
        return read, 201

    @marshal_with(resources_fields)
    def patch(self, user_id):
        args = issue_update_args.parse_args()
        result = IssueModel.query.filter_by(id= user_id).first()
        if not result:
            abort(404, message='No issue with given ID is found')

        if args['issue']:
            result.issue = args['issue']
        if args['type']:
            result.type = args['type']

        db.session.commit()

        return result


api.add_resource(IssueRead, "/channel/<int:user_id>")

if __name__ == '__main__':
    app.run(debug=True)