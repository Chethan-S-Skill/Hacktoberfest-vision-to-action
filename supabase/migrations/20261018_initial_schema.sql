-- ==============================================================================
-- REALITY -> ACTION AI: DATABASE SCHEMA & ROW LEVEL SECURITY (RLS) POLICIES
-- ==============================================================================

-- 1. Create analysis_history table
create table if not exists public.analysis_history (
    id uuid primary key default gen_random_uuid(),
    user_id uuid references auth.users(id) on delete cascade not null,
    question text not null,
    image_path text,
    ai_response jsonb not null,
    model_name text not null default 'sarvam-gemma-4',
    threat_level text not null default 'LOW',
    status text not null default 'completed',
    created_at timestamptz not null default now()
);

-- 2. Indexes for fast user queries and timeline ordering
create index if not exists idx_analysis_history_user_id 
    on public.analysis_history(user_id);

create index if not exists idx_analysis_history_created_at 
    on public.analysis_history(created_at desc);

-- 3. Enable Row Level Security (RLS)
alter table public.analysis_history enable row level security;

-- Drop existing policies if re-running
drop policy if exists "Users can view own analyses" on public.analysis_history;
drop policy if exists "Users can insert own analyses" on public.analysis_history;
drop policy if exists "Users can delete own analyses" on public.analysis_history;

-- 4. Strict user-isolated RLS policies
create policy "Users can view own analyses"
    on public.analysis_history
    for select
    using (auth.uid() = user_id);

create policy "Users can insert own analyses"
    on public.analysis_history
    for insert
    with check (auth.uid() = user_id);

create policy "Users can delete own analyses"
    on public.analysis_history
    for delete
    using (auth.uid() = user_id);

-- ==============================================================================
-- 5. STORAGE BUCKET: reality-images (Private Storage with isolated user folders)
-- ==============================================================================

-- Insert private bucket if not exists
insert into storage.buckets (id, name, public)
values ('reality-images', 'reality-images', false)
on conflict (id) do update set public = false;

-- Storage RLS: Ensure storage objects table has RLS enabled
alter table storage.objects enable row level security;

drop policy if exists "Users can upload own images" on storage.objects;
drop policy if exists "Users can view own images" on storage.objects;
drop policy if exists "Users can delete own images" on storage.objects;

-- Allow authenticated users to upload only into their own user_id directory
create policy "Users can upload own images"
    on storage.objects
    for insert
    with check (
        bucket_id = 'reality-images'
        and auth.role() = 'authenticated'
        and (storage.foldername(name))[1] = auth.uid()::text
    );

-- Allow authenticated users to read only their own images
create policy "Users can view own images"
    on storage.objects
    for select
    using (
        bucket_id = 'reality-images'
        and auth.role() = 'authenticated'
        and (storage.foldername(name))[1] = auth.uid()::text
    );

-- Allow authenticated users to delete only their own images
create policy "Users can delete own images"
    on storage.objects
    for delete
    using (
        bucket_id = 'reality-images'
        and auth.role() = 'authenticated'
        and (storage.foldername(name))[1] = auth.uid()::text
    );
