import os
import flask
import zipfile
from pydatamocker import from_dict
import tempfile


app = flask.Flask(__name__)


@app.route('/schema', methods=['POST'])
async def root():
    if (req_data := flask.request.json):
        sch = from_dict(req_data)
        sch.sample()
        files = {}
        for table in sch.tables.values():
            data = table._data
            file = tempfile.NamedTemporaryFile(prefix=table._name, suffix='.csv', delete=False)
            data.to_csv(file, index=False)
            files[table._name] = file
        aggregate  = tempfile.NamedTemporaryFile('w+', delete=False)
        with zipfile.ZipFile(aggregate.name, 'w') as f:
            for name, file in files.items():
                f.write(file.name, f'{name}.csv', compress_type=zipfile.ZIP_DEFLATED)
        res = flask.send_file(aggregate.name, download_name='schema.zip')
        res.status_code = 200
        for file in files.values():
            file.close()
        aggregate.close()
        return res
