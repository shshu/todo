import enum

from app import db


class SevirityType(enum.Enum):
    CRITICAL = 1 # A critical incident with very high impact
    MAJOR = 2 # A major incident with significant impact
    REGULAR = 3 # Regular
    MINOR = 4  # A minor incident with low impact

class Task(db.Model):
    __tablename__ = 'task'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    task = db.Column(db.String(120), nullable=False)
    is_done = db.Column(db.Boolean, default=False, nullable=False)
    severity = db.Column(db.Enum(SevirityType), default=SevirityType.REGULAR , nullable=False)

    def __init__(self, task):
        self.task = task

    def __repr__(self):
        return '<id {}>'.format(self.id)
