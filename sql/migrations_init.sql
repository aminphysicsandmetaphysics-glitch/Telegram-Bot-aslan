-- run this once in Supabase SQL editor
-- users/payments/subscriptions/giveaways/giveaway tasks/entries + app_settings/channels/socials

-- users
create table if not exists users (
  id bigserial primary key,
  tg_id bigint unique not null,
  username text,
  first_name text,
  last_name text,
  is_vip boolean default false,
  vip_until timestamptz,
  created_at timestamptz default now()
);

-- payments
create table if not exists payments (
  id bigserial primary key,
  user_id bigint references users(id) on delete set null,
  provider text default 'crypto',
  amount numeric,
  currency text default 'USDT',
  status text default 'pending',
  tx_id text,
  meta jsonb default '{}'::jsonb,
  created_at timestamptz default now()
);
create index if not exists idx_payments_tx on payments(tx_id);

-- subscriptions
create table if not exists subscriptions (
  id bigserial primary key,
  user_id bigint references users(id) on delete cascade,
  plan text,
  status text default 'active',
  started_at timestamptz default now(),
  ends_at timestamptz
);

-- giveaways
create table if not exists giveaways (
  id bigserial primary key,
  title text,
  description text,
  is_active boolean default true,
  starts_at timestamptz default now(),
  ends_at timestamptz
);

create table if not exists giveaway_tasks (
  id bigserial primary key,
  giveaway_id bigint references giveaways(id) on delete cascade,
  task_type text not null,
  target text,
  weight int default 1,
  is_required boolean default true
);

create table if not exists giveaway_entries (
  id bigserial primary key,
  giveaway_id bigint references giveaways(id) on delete cascade,
  user_id bigint references users(id) on delete cascade,
  points int default 0,
  created_at timestamptz default now(),
  unique (giveaway_id, user_id)
);

-- settings/channel/social links
create table if not exists app_settings (key text primary key, value text not null, updated_at timestamptz default now());
create table if not exists channels (id bigserial primary key, kind text not null, handle text not null);
create table if not exists social_links (id bigserial primary key, platform text not null, url text not null);
