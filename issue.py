import json
from pathlib import Path

from google.fhir.r4 import json_format
from proto.google.fhir.proto.r4.core.resources.bundle_and_contained_resource_pb2 import (  # noqa: E501
    Bundle,
)

LPR = Path("25dc5040-5875-8486-a49c-ed4789b7c88c.json")

lpr_json = LPR.read_text()

original_lpr = json.loads(lpr_json)

bundle = json_format.json_fhir_string_to_proto(lpr_json, Bundle)

new_lpr_json = json_format.pretty_print_fhir_to_json_string(bundle)

new_lpr = json.loads(new_lpr_json)

print(new_lpr_json)
