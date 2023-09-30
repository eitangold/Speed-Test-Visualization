class SpeedTestParser:
   def __init__(self,speed_test_result:dict[str:str]) -> None:
      download = speed_test_result.get('download',None)
      if not download:
         raise ValueError("Download parameter dosn't exist in the speed test result json")
      download_bytes_speed = download.get('bytes',None)
      if not download_bytes_speed:
         raise ValueError("The value bytes doesn't exist in the result json")
      self.download_speed = download_bytes_speed/1000000
      
      
      upload = speed_test_result.get('upload',None)
      if not upload:
         raise ValueError("upload parameter dosn't exist in the speed test result json")
      upload_bytes_speed = upload.get('bytes',None)
      if not upload_bytes_speed:
         raise ValueError("The value bytes doesn't exist in the result json")
      self.upload_speed = upload_bytes_speed/1000000

   def get_download_speed(self) -> float:
      return self.download_speed
   
   def get_upload_speed(self) -> float:
      return self.upload_speed
   