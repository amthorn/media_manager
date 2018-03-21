import requests
ids = ["tt1049413", "tt0387564", "tt0114709", "tt0120363", "tt0435761",
       "tt0113862", "tt0332280", "tt0109830", "tt0266543", "tt2277860"]
for id in ids:
    result = requests.post(f'http://0.0.0.0:9999/api/v1/movies', json={'IMDBID': id})
    print(id)

# add all
# for id in range(10000000):
#     result = requests.get(f'http://0.0.0.0:9999/api/v1/movies/add_by_id/tt{id}')
#     print(id)
