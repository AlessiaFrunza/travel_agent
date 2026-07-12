-- -----------------------------------------------------------------------------
-- ENUMS
-- Define allowed values for typed columns before using them in tables
-- -----------------------------------------------------------------------------
 
CREATE TYPE attraction_type AS ENUM (
    'museum',
    'park',
    'restaurant',
    'landmark',
    'beach',
    'shopping',
    'entertainment',
    'sport',
    'other'
);
 
CREATE TYPE destination_type AS ENUM (
    'city',
    'beach',
    'mountain',
    'countryside',
    'island',
    'other'
);



CREATE TABLE "User" (
    usr_id      SERIAL          PRIMARY KEY,
    first_name  VARCHAR(50)     NOT NULL,
    last_name   VARCHAR(50)     NOT NULL,
    email       VARCHAR(100)    NOT NULL UNIQUE,
    birth_date  DATE,
    phone       VARCHAR(20),
    address     VARCHAR(100),
    created_at  TIMESTAMP       NOT NULL DEFAULT NOW()
);

CREATE TABLE "Destination" (
    destination_id  SERIAL          PRIMARY KEY,
    city            VARCHAR(100)    NOT NULL,
    country         VARCHAR(100)    NOT NULL,
    type            destination_type
);

CREATE TABLE "Attraction" (
    attraction_id   SERIAL          PRIMARY KEY,
    destination_id  INT             NOT NULL REFERENCES "Destination"(destination_id) ON DELETE CASCADE,
    name            VARCHAR(150)    NOT NULL,
    type            attraction_type NOT NULL
);

CREATE TABLE "Hotel" (
    hotel_id        SERIAL          PRIMARY KEY,
    destination_id  INT             NOT NULL REFERENCES "Destination"(destination_id) ON DELETE RESTRICT,
    name            VARCHAR(150)    NOT NULL,
    rating          NUMERIC(2,1)    CHECK (rating >= 0 AND rating <= 5),
    address         VARCHAR(150),
    contact         VARCHAR(20)
);

CREATE TABLE "Flight" (
    flight_id       SERIAL          PRIMARY KEY,
    airline         VARCHAR(100),
    origin_city     VARCHAR(100)    NOT NULL,
    destination_city VARCHAR(100)   NOT NULL,
    departure_at    TIMESTAMP       NOT NULL,
    arrival_at      TIMESTAMP       NOT NULL
);

CREATE TABLE "Trip" (
    trip_id     SERIAL          PRIMARY KEY,
    usr_id      INT             NOT NULL REFERENCES "User"(usr_id) ON DELETE CASCADE,
    name        VARCHAR(150),
    budget      NUMERIC(10,2)   CHECK (budget >= 0),
    start_date  DATE            NOT NULL,
    end_date    DATE            NOT NULL,
    num_day     INT             GENERATED ALWAYS AS (end_date - start_date) STORED,
    created_at  TIMESTAMP       NOT NULL DEFAULT NOW(),
    CHECK (end_date >= start_date)
);

CREATE TABLE "Trip_Destination" (
    trip_id         INT     NOT NULL REFERENCES "Trip"(trip_id) ON DELETE CASCADE,
    destination_id  INT     NOT NULL REFERENCES "Destination"(destination_id) ON DELETE RESTRICT,
    PRIMARY KEY (trip_id, destination_id)
);

CREATE TABLE "Booking" (
    booking_id  SERIAL      PRIMARY KEY,
    trip_id     INT         NOT NULL REFERENCES "Trip"(trip_id) ON DELETE CASCADE,
    flight_id   INT         REFERENCES "Flight"(flight_id) ON DELETE SET NULL,
    hotel_id    INT         REFERENCES "Hotel"(hotel_id) ON DELETE SET NULL,
    booked_at   TIMESTAMP   NOT NULL DEFAULT NOW(),
    CHECK (flight_id IS NOT NULL OR hotel_id IS NOT NULL)  -- at least one must be booked
);

 
CREATE TABLE "Daily_Itinerary" (
    day_num         INT     NOT NULL,
    trip_id         INT     NOT NULL REFERENCES "Trip"(trip_id) ON DELETE CASCADE,
    destination_id  INT     NOT NULL REFERENCES "Destination"(destination_id) ON DELETE RESTRICT,
    attraction_id   INT     REFERENCES "Attraction"(attraction_id) ON DELETE SET NULL,
    notes           TEXT,
    PRIMARY KEY (day_num, trip_id)
);