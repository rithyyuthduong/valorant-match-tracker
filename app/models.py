import sqlalchemy as sa
import sqlalchemy.orm as so
from app import db
from datetime import datetime, timezone
from typing import Optional

class Match(db.Model):
    id: so.Mapped[int] = so.mapped_column(primary_key=True)
    date_played: so.Mapped[Optional[datetime]] = so.mapped_column(
        default=lambda: datetime.now(timezone.utc)
    )
    kills: so.Mapped[int] = so.mapped_column(sa.Integer, index=True)
    deaths: so.Mapped[int] = so.mapped_column(sa.Integer, index=True)
    agent: so.Mapped[str] = so.mapped_column(sa.String(28), index=True)
    map: so.Mapped[str] = so.mapped_column(sa.String(28), index=True)
    rr_change: so.Mapped[int] = so.mapped_column(sa.Integer, index=True)
    result: so.Mapped[bool] = so.mapped_column(sa.Boolean)
    assists: so.Mapped[int] = so.mapped_column(sa.Integer, index=True)
    my_team_score: so.Mapped[int] = so.mapped_column(sa.Integer, index=True)
    enemy_team_score: so.Mapped[int] = so.mapped_column(sa.Integer, index=True)
    rank_after: so.Mapped[str] = so.mapped_column(sa.String(28), index=True)
    rank_before: so.Mapped[str] = so.mapped_column(sa.String(28), index=True)
    
    def __repr__(self):
         return '<Match {} - {}>'.format(self.agent, self.result)