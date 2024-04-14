import config.environment

# ! Overwrite our db_URI with this one, which flask will use when it runs. It's an In-memory sqllite database.
# ! Make sure the variable its overwriting matches your variable in config/environment.py!
config.environment.db_URI = "sqlite://"