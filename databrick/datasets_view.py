from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from datasets import load_dataset
import logging

logger=logging.getLogger('databrick')
class DatabrickContextAPIView(APIView):
    def get(self,request):
        dataset=load_dataset("json",data_files="data/databricks-dolly-15k-with-tags.jsonl")
        train_ds=dataset['train']
        df=train_ds.to_pandas()
        ctx_df=df[df['context']!=""]
        ctx_df=ctx_df.sort_values('response_noun_tags_count',ascending=False)
        filtered_data=ctx_df.to_dict('records')
        logger.info(f"filtered data has {len(filtered_data)} records")
        return Response(filtered_data,status=status.HTTP_200_OK)
