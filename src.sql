DROP TABLE IF EXISTS artists;

CREATE TABLE artists (
    ConstituentID TEXT PRIMARY KEY,
    DisplayName TEXT,
    ArtistBio TEXT,
    Nationality TEXT,
    Gender TEXT,
    BeginDate INT,
    EndDate INT,
    Wiki_QID TEXT,
    ULAN TEXT
);

\copy artists FROM 'Artists.csv' WITH (FORMAT csv, HEADER true);