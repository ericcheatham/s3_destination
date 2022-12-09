import hashlib
import logging
import sys

from turbine.runtime import RecordList
from turbine.runtime import Runtime

logging.basicConfig(level=logging.INFO)



def do_the_thing(records: RecordList) -> RecordList:
    return records

class App:
    @staticmethod
    async def run(turbine: Runtime):
        try:
        
            source = await turbine.resources("notion")

            records = await source.records("",{"pollInterval": "5m"})

            thinged = await turbine.process(records, do_the_thing)

            destination_db = await turbine.resources("s3")

            await destination_db.write(thinged, "new_notion_dest", {})
        except Exception as e:
            print(e, file=sys.stderr)
