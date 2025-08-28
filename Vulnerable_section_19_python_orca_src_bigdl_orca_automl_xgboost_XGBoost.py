 # limitations under the License.
 #
 
import pickle
 
 import pandas as pd
 from xgboost.sklearn import XGBRegressor
         return result_list
 
     def save(self, checkpoint):
        pickle.dump(self.model, open(checkpoint, "wb"))
 
     def restore(self, checkpoint):
         with open(checkpoint, 'rb') as f:
            self.model = pickle.load(f)
         self.model_init = True
 
     def _get_required_parameters(self):