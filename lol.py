from riotwatcher import LolWatcher, ApiError
lol_watcher = LolWatcher(api_key = 'RGAPI-45ef8755-23a2-4a5a-a5f0-a5196362e845')
region = 'euw1'
Swangkawaii = lol_watcher.summoner.by_name(region, 'Swangkawaii')
Eclésya     = lol_watcher.summoner.by_name(region, 'Eclésya')