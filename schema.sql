-- Uncomment following for testing -> results in overwrite:
DROP TABLE IF EXISTS project_time_logs CASCADE;
DROP TABLE IF EXISTS projects CASCADE;

-- Extensions
CREATE EXTENSION IF NOT EXISTS pgcrypto;

-- ===================
-- Projects table
-- ===================
CREATE TABLE IF NOT EXISTS projects (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    name TEXT NOT NULL,
    owner_id TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE INDEX IF NOT EXISTS idx_projects_owner_id
    ON projects (owner_id);

-- ===================
-- Project time logs
-- ===================
CREATE TABLE IF NOT EXISTS project_time_logs (
    id UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    project_id UUID NOT NULL
        REFERENCES projects(id)
        ON DELETE CASCADE,
    owner_id TEXT NOT NULL,
    started_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    ended_at TIMESTAMPTZ
);

CREATE INDEX IF NOT EXISTS idx_time_logs_project_id
    ON project_time_logs (project_id);

CREATE INDEX IF NOT EXISTS idx_time_logs_owner_id
    ON project_time_logs (owner_id);

-- Only one timer per project/user
CREATE INDEX IF NOT EXISTS idx_time_logs_open
    ON project_time_logs (project_id, owner_id)
    WHERE ended_at IS NULL;
