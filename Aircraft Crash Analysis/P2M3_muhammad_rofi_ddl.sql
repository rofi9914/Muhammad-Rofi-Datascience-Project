-- MEMBUAT TABEL SESUAI DENGAN KOLOM
CREATE TABLE tabel_m3 (
	record_id VARCHAR(100),
	aircraft_type VARCHAR(100),
	airport_name VARCHAR(100),
	altitude_bin VARCHAR(100),
	aircraft_make_model VARCHAR(100),
	wildlife_number_struck VARCHAR(100),
	wildlife_number_struck_actual VARCHAR(100),
	effect_impact_to_flight VARCHAR(200),
	flightdate VARCHAR(100),
	effect_indicated_damage VARCHAR(100),
	aircraft_number_of_engines VARCHAR(100),
	aircraft_airline_operator VARCHAR(100),
	origin_state VARCHAR(100),
	when_phase_of_flight VARCHAR(100),
	conditions_precipitation VARCHAR(100),
	remains_of_wildlife_collected VARCHAR(100),
	remains_of_wildlife_sent_to_smithsonian VARCHAR(100),
	remarks VARCHAR(300),
	wildlife_size VARCHAR(100),
	conditions_sky VARCHAR(100),
	wildlife_species VARCHAR(100),
	pilot_warned_of_birds_or_wildlife VARCHAR(100),
	cost_total VARCHAR(100),
	feet_above_ground VARCHAR(100),
	number_of_people_injured VARCHAR(100),
	is_aircraft_large VARCHAR(100)
);

-- MEMBACA CSV
COPY tabel_m3 (
	record_id,
	aircraft_type,
	airport_name,
	altitude_bin,
	aircraft_make_model,
	wildlife_number_struck,
	wildlife_number_struck_actual,
	effect_impact_to_flight,
	flightdate,
	effect_indicated_damage,
	aircraft_number_of_engines,
	aircraft_airline_operator,
	origin_state,
	when_phase_of_flight,
	conditions_precipitation,
	remains_of_wildlife_collected,
	remains_of_wildlife_sent_to_smithsonian,
	remarks,
	wildlife_size,
	conditions_sky,
	wildlife_species,
	pilot_warned_of_birds_or_wildlife,
	cost_total,
	feet_above_ground,
	number_of_people_injured,
	is_aircraft_large
)
FROM 'D:\Hacktiv8\Phase2\Milestone\bird_strikes.csv'
DELIMITER ','
CSV HEADER;

-- TAMPILKAN TABLE
SELECT * FROM tabel_m3  