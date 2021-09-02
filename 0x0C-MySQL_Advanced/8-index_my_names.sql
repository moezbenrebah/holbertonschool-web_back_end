-- creates an index on a table that match the first letter of a given name

CREATE INDEX `idx_name_first` ON names (name(1));
