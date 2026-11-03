from datetime import datetime, timezone
from database.database import db


class AccessSession(db.Model):
    __tablename__ = "access_sessions"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=False, index=True)
    ip_address = db.Column(db.String(64), nullable=True)
    login_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    logout_at = db.Column(db.DateTime, nullable=True)
    last_seen = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)


class SystemLog(db.Model):
    __tablename__ = "system_logs"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), nullable=True)
    event_type = db.Column(db.String(50), nullable=False)
    details = db.Column(db.Text, nullable=True)
    ip_address = db.Column(db.String(64), nullable=True)
    created_at = db.Column(db.DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

