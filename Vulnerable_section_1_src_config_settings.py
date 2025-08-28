     ALLOWED_HOSTS=(str, ""),
     AWS_STORAGE_BUCKET_NAME=(str, "hellopy-bucket"),
     AWS_S3_REGION_NAME=(str, "ap-northeast-2"),
 )
 
 environ.Env.read_env(BASE_DIR / ".env")
 
 ALLOWED_HOSTS = env("ALLOWED_HOSTS").split(",")
 
 # 외부 라이브러리 (Third-party Apps)
 THIRD_PARTY_APPS = [
     "rest_framework",