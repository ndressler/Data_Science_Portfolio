-- Create indexes
CREATE INDEX idx_glas_gname ON glas(GNAME);

CREATE INDEX idx_cocktail_cname ON cocktail(CNAME);
CREATE INDEX idx_cocktail_gid ON cocktail(GID);
CREATE INDEX idx_cocktail_alcohol ON cocktail(ALKOHOLISCH);

CREATE INDEX idx_ingredient_zname ON ingredient(ZNAME);

CREATE INDEX idx_local_plz ON local(PLZ);
CREATE INDEX idx_local_stadt ON local(STADT);

CREATE INDEX idx_person_name ON person(NAME);
CREATE INDEX idx_person_gebdat ON person(GEBURTSDATUM);

CREATE INDEX idx_cocktail_local_cid ON cocktail_local(CID);
CREATE INDEX idx_cocktail_local_lid ON cocktail_local(LID);

CREATE INDEX idx_cocktail_person_cid ON cocktail_person(CID);
CREATE INDEX idx_cocktail_person_pid1 ON cocktail_person(PID1);
CREATE INDEX idx_cocktail_person_pid2 ON cocktail_person(PID2);

CREATE INDEX idx_ingredient_cocktail_zid ON ingredient_cocktail(ZID);
CREATE INDEX idx_ingredient_cocktail_cid ON ingredient_cocktail(CID);
