class KwonStringCleaner:
    @staticmethod
    def clean(txt):
        txt = txt.replace("<b>", "")
        txt = txt.replace("</b>", "")
        txt = txt.replace("&quot;", "")
        return txt
    
# <b></b>처리하는게 네이버뿐만 아니라, 카카오, ...
#   지금 처리 -> 나중에도 필요할듯 -> 회사가서도
#   -> 처리하기 편하게 정리 좀

# library vs framework
#   library
#       자주 쓸것같은 기능 따로 정리
#       파일(패키지) 통째로 갖고다니면서
#       필요할때마다 쓰기 편하게
#   framework
#       library + 자체개발툴
#       대충 잘 구별안하는...