 from api.utils.api_utils import get_json_result
 from rag.llm import EmbeddingModel, ChatModel, RerankModel,CvModel
 import requests
 
 @manager.route('/factories', methods=['GET'])
 @login_required
     if factory == "VolcEngine":
         # For VolcEngine, due to its special authentication method
         # Assemble volc_ak, volc_sk, endpoint_id into api_key
        temp = list(eval(req["llm_name"]).items())[0]
         llm_name = temp[0]
         endpoint_id = temp[1]
         api_key = '{' + f'"volc_ak": "{req.get("volc_ak", "")}", ' \