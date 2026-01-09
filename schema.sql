-- Uncomment following for testing -> results in overwrite:
-- DROP TABLE IF EXISTS projects CASCADE;

-- Extensions
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- Projects table
CREATE TABLE IF NOT EXISTS projects (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    owner_id TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

-- Search structure
CREATE INDEX IF NOT EXISTS idx_projects_owner_id
    ON projects (owner_id);
