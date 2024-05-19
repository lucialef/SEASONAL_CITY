from flask import Flask, render_template, request
from flask import jsonify
import seasonal

app = Flask(__name__)

@app.route('/')
@app.route('/index')
@app.route('/home')
def index():
	return render_template('index.html')


@app.route('/info', methods=['GET', 'POST'])
def process_post():
  coord_start = request.form['start_pt']
  coord_end = request.form['end_pt']
  sel_month = request.form['sel_month']

  data_fin = seasonal.getRoutes(sel_month, coord_start, coord_end)
  
  # season_path_geojson, short_path_geojson, tr_season_geojson, orig_address_geojson, dest_address_geojson
  season_path_gj = data_fin[0]
  short_path_gj = data_fin[1]
  tr_season_gj = data_fin[2]
  orig_address_gj = data_fin[3]
  dest_address_gj = data_fin[4]
  short_km_gj = data_fin[5]
  short_time_gj = data_fin[6]
  seas_km_gj = data_fin[7]
  seas_time_gj = data_fin[8]

  return render_template('index2.html', 
    orig=orig_address_gj, dest=dest_address_gj, short_path=short_path_gj, season_path=season_path_gj, 
    tr_season=tr_season_gj, short_km=short_km_gj, short_time=short_time_gj, seas_km=seas_km_gj, seas_time=seas_time_gj)


if __name__ == '__main__':
  app.run(debug=True)