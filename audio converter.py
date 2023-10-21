import os
def main():
  # common audio file formats
  valid_formats = [".mp3",".flac",".wav",".m4a",".ogg","aiff",".acc"]
  read_format = '.' + input("Enter the file format to convert from:\n\t").strip('.')
  # check against list of valid formats to make sure the end user is not providing 
  # useless info that will cause ffmpeg to error
  if read_format not in valid_formats:
    print("ERROR... Invalid/Unsupported File Format")
    return 0
  write_format = '.' + input("Enter the file format to convert to:\n\t").strip('.')
  # same error check as last
  if write_format not in valid_formats:
    print("ERROR... Invalid/Unsupported File Format")
    return 0
  # get folder from user, invert backlashes if apply to help prevent errors
  folder_directory = (input("Enter the path to the folder containing the files:\n\t")).replace('\\','/')
  # test if valid directory, if os.chrdir() fail directory most likely does not exist
  try:
    os.chdir(folder_directory)
  # error message and exit
  except:
    print("ERROR... Program Can Not Find/Does Not Have Access To Folder")
    return 0
  # get list of files in directory
  all_files = os.listdir(path = folder_directory)
  # get list of files that have the valid read format
  valid_files = []
  for file in all_files:
    if file[-len(read_format):] == read_format:
      valid_files.append(file)
  # remove file format from stored files names
  for index, file in enumerate(valid_files):
    valid_files[index] = file[:-len(read_format)]
  # create new directory to house converted files
  os.mkdir("converted")
  # go through list of valid files and use ffmpeg to convert to the desired format
  for file in valid_files:
    os.system('ffmpeg -i "'+file+read_format+'" "'+folder_directory+'/converted/'+file+write_format+'"')
main()