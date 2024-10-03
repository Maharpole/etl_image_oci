import oci
import io

def handler(ctx, data: io.BytesIO = None):
    signer = oci.auth.signers.get_resource_principals_signer()
    
    # Example: List objects in an OCI Object Storage bucket
    object_storage_client = oci.object_storage.ObjectStorageClient(config={}, signer=signer)
    namespace = object_storage_client.get_namespace().data
    bucket_name = "your_bucket_name"
    
    objects = object_storage_client.list_objects(namespace, bucket_name)
    for obj in objects.data.objects:
        print(obj.name)
    
    return "Function executed successfully"
