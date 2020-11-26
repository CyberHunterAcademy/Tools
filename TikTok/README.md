# TikTok OSINT

Tool for recover information about a profile on tiktok platform

## Instalation

``` 
svn checkout https://github.com/CyberHunterAcademy/Tools/trunk/TikTok

pip3 install -r requirements
```

## Usage

Get information about one tiktok profile:
```
python3 get_info_tiktok.py -u url_tiktok_profile
```

Write results to a csv:
```
python3 get_info_tiktok.py -u url_tiktok_profile -f file.csv
```

Search for a list of profiles (one per line):
```
python3 get_info_tiktok.py -r request_file
```


![](Docs/FunctionsGetInfoTikTok.gif)
