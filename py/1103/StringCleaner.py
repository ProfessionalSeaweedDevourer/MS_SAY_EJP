# 불필요한 태그를 데이터에서 일괄 제거.

# 라이브러리 vs 프레임워크: 어디서나 자주 쓸 것 같은 기능을 따로 만들어서 정리해 두기.
#   library: 자주 쓰는 기능을 뭉쳐 둔 패키지.
#   framework: 라이브러리와 자체적인 개발 도구를 포함. 사실 구별이 애매한 편

class StringClearner:
    @staticmethod
    def clean(txt):
        txt = txt.replace("<b>", "")
        txt = txt.replace("</b>", "")
        txt = txt.replace("&quot", "")
        return txt