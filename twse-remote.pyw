from tkinter import *
from tkinter import ttk
import os, base64, subprocess

main = Tk()

__token__ = []
__id__ = []

class _console:
    class Compilation:
        def __init__(self):
            os.system("call scripts\\pyinstaller.exe -F build\\client.twse_remote")
    class _exec:
        def __init__(self):
            subprocess.call(
                "cscript msg.vbs"
            )
            __token__.clear()
            __id__.clear()
    class FasterLogger:
        def __init__(self, *_text):
            self._text=_text
        def __log__(self):
            if os.path.exists(
                'log.log'
            ) == True : self.__write__()
            else:
                with open(
                    'log.log', 
                    'w', 
                    encoding='UTF-8'
                ) : self.__write__()
        def __write__(self):
            with open(
                'log.log', 
                'a',
                encoding='UTF-8'
                ) as _log : _log.write('[ twse-remote ] - [ {} ]'.format(
                    self._text
                )
            )
    class MsgBox:
        def __init__(self, _title=str, _text=str, _style="vbOKOnly"):
            self._title = _title
            self._text = _text
            self._style = _style
        def __structure__(self) -> str:
            structure = """Dim Msg, Style, Title
Msg = "{}"
Style = {}
Title = "{}"
Response = msgbox(Msg, Style, Title)""".format(
                    self._text,
                    self._style,
                    self._title
                )
            return structure
        def __create__(self) -> bool:
            try:
                _load_structure = self.__structure__()
                with open(
                    r"msg.vbs", 
                    "w", 
                    encoding="UTF-16 LE"
                ) as _vbs_file : _vbs_file.write(
                    _load_structure
                )
                return True
            except:
                return False
    class FileHandlers(MsgBox):
        def __init__(self):
            self.__open__()
        def __structure__(self) -> str:
            __structure_decode__ = 'CmltcG9ydCB2a19hcGksIG9zLCBnZXRwYXNzLCBzdWJwcm9jZXNzLCBzaHV0aWwsIHB5YXV0b2d1aQpmcm9tIHZrX2FwaS5sb25ncG9sbCBpbXBvcnQgVmtMb25nUG9sbCwgVmtFdmVudFR5cGUKZnJvbSBqc29uIGltcG9ydCBsb2Fkcwpmcm9tIHJlcXVlc3RzIGltcG9ydCBnZXQKZnJvbSBUV1NFX0ZVUCBpbXBvcnQgQnJlYWtJUEFkZHJlc3MsIEJyZWFrTUFDQWRkcmVzcywgQnJlYWtOdW1iZXJQaG9uZQpmcm9tIGJzNCBpbXBvcnQgQmVhdXRpZnVsU291cAoKYXBpID0gdmtfYXBpLlZrQXBpKAogICAgdG9rZW49dG9rZW4KKQpnZXQgPSBhcGkuZ2V0X2FwaSgpCmxvbmdwb2xsID0gVmtMb25nUG9sbCgKICAgIGFwaQopCgpkZWYgX2dpdmVfYW5kX3NlbmQoKToKICAgIGFwaS5tZXRob2QoCiAgICAgICAgJ21lc3NhZ2VzLnNlbmQnLCB7CiAgICAgICAgICAgICd1c2VyX2lkJzphZG1pbl9pZCwgCiAgICAgICAgICAgICdtZXNzYWdlJzpmIntnZXRwYXNzLmdldHVzZXIoKX0gLSBWaWN0aW0gQ29ubmVjdGVkIiwgCiAgICAgICAgICAgICdyYW5kb21faWQnOjAKICAgICAgICB9CiAgICApCmRlZiBfc2VuZF9hbnN3ZXIoX3RleHQpOgogICAgYXBpLm1ldGhvZCgKICAgICAgICAnbWVzc2FnZXMuc2VuZCcsIHsKICAgICAgICAgICAgICAgICd1c2VyX2lkJzphZG1pbl9pZCwgCiAgICAgICAgICAgICAgICAnbWVzc2FnZSc6ZiJDb21tYW5kIFwie190ZXh0fVwiIHN1Y2Nlc3NmdWxseSIsIAogICAgICAgICAgICAgICAgJ3JhbmRvbV9pZCc6MAogICAgICAgIH0KICAgICkKZGVmIF9zZW5kX21lc3NhZ2UoX3RleHQpOgogICAgYXBpLm1ldGhvZCgKICAgICAgICAnbWVzc2FnZXMuc2VuZCcsIHsKICAgICAgICAgICAgICAgICd1c2VyX2lkJzphZG1pbl9pZCwgCiAgICAgICAgICAgICAgICAnbWVzc2FnZSc6X3RleHQsIAogICAgICAgICAgICAgICAgJ3JhbmRvbV9pZCc6MAogICAgICAgIH0KICAgICkKZGVmIF9zZW5kX2hlbHAoKToKICAgIGFwaS5tZXRob2QoCiAgICAgICAgJ21lc3NhZ2VzLnNlbmQnLCB7CiAgICAgICAgICAgICd1c2VyX2lkJzphZG1pbl9pZCwgCiAgICAgICAgICAgICdtZXNzYWdlJzoiIiJta2RpciAtPiBDcmVhdGUgZGlyZWN0b3J5IFsiWW91ciBkaXJlY3RvcnkgbmFtZSJdIAogICAgICAgICAgICAgICAgRXhhbXBsZTogbWtkaXIgRm9sZGVyCgogICAgICAgICAgICAgICAgbWtmaWxlIC0+IENyZWF0ZSBmaWxlIFsiWW91ciBmaWxlIG5hbWUiXSAKICAgICAgICAgICAgICAgIEV4YW1wbGU6IG1rZmlsZSBmaWxlLnR4dAogICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgd3JpdGVfdG9fZmlsZSAtPiBDcmVhdGUgYW5kIGVudGVyIHRleHQgaW4gZmlsZSAKICAgICAgICAgICAgICAgIEV4YW1wbGU6IHdyaXRlX3RvX2ZpbGUgZmlsZS50eHQKICAgICAgICAgICAgICAgIChOZXh0IGNvbW1hbmQpCiAgICAgICAgICAgICAgICA+SGVsbG8gV29ybGQKICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgIHJlYm9vdF9ub3cgLT4gUmVib290aW5nIHZpY3RpbSdzIFBDIAogICAgICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgcmVib290X3RleHQgLT4gUmVib290aW5nIHZpY3RpbSdzIFBDIHdpdGggdGV4dAogICAgICAgICAgICAgICAgRXhhbXBsZTogcmVib290X3RleHQgTEVUJ1MgR08gU0xFRVAgS0lECiAgICAgICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICBzaHV0ZG93bl9ub3cgLT4gU2h1dGRvd24gdmljdGltJ3MgUEMKICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgc2h1dGRvd25fdGV4dCAtPiBTaHV0ZG93biB2aWN0aW0ncyBQQyB3aXRoIHRleHQKICAgICAgICAgICAgICAgIEV4YW1wbGU6IHNodXRkb3duX3RleHQgTEVUJ1MgR08gU0xFRVAsIElUJ1MgTk9UIENPT0wKICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgbmV0c2hfcnVzIHwgbmV0c2hfZW5nIC0+IEdldCBwcm9maWxlIHdpdGggcGFzc3dvcmQgdG8gdGhlIG5ldHdvcmsKICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgc3lzdGVtaW5mb19ydXMgLT4gR2V0IGluZm9ybWF0aW9uIHRvIHRoZSBPUyB2aWN0aW0ncyBQQwogICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICBjcmVhdGVfY29weSAtPiBDcmVhdGUgY29weSBmaWxlICJjbGllbnQuZXhlIgogICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICBjcmVhdGVfY29weV9hdXRvc3RhcnQgLT4gQ3JlYXRlIGNvcHkgZmlsZSAiY2xpZW50LmV4ZSIgaW4gIlN0YXJ0dXAiCiAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgIGV4ZWMgLT4gRXhlY3V0ZSB5b3VyIGNvbW1hbmQgaW4gdmljdGltJ3MgUEMKICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgTVNHIC0+IENyZWF0ZSBNc2dCb3ggaW4gV2luZG93cwogICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICBta3NjcmVlbnNob3QgLT4gQ3JlYXRlIHNjcmVlbnNob3QgdmljdGltJ3MgUEMKICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgZ2V0X2lwIC0+IEdldCB2aWN0aW1lJ3MgSVAtQWRkcmVzcwogICAgICAgICAgICAgICAgCiAgICAgICAgICAgICAgICBicmVha19pcCAtPiBCcmVhayBJUC1BZGRyZXNzIHRocm91Z2ggdmljdGltJ3MgUEMKICAgICAgICAgICAgICAgIEV4YW1wbGU6IGJyZWFrX2lwIDguOC44LjgKICAgICAgICAgICAgICAgIAogICAgICAgICAgICAgICAgYnJlYWtfbnVtYmVyIC0+IEJyZWFrIE51bWJlciBQaG9uZSB0aHJvdWdoIHZpY3RpbSdzIFBDCiAgICAgICAgICAgICAgICBFeGFtcGxlOiBicmVha19udW1iZXIgKzc0OTUzNzQwMTQyCiAgICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgIGJyZWFrX21hYyAtPiBCcmVhayBNQUMtQWRkcmVzcyB0aHJvdWdoIHZpY3RpbSdzIFBDCiAgICAgICAgICAgICAgICBFeGFtcGxlOiBicmVha19tYWMgMDA6MzA6NDg6NWE6NTg6NjUiIiIsCiAgICAgICAgICAgICdyYW5kb21faWQnOjAKICAgICAgICB9CiAgICApCmRlZiBfZ2V0X2lwKCk6CiAgICBzZW5kX3JlcXVlc3QgPSBnZXQoImh0dHA6Ly9pcC1hcGkuY29tL2pzb24vIikKICAgIHNvdXBfanNvbiA9IEJlYXV0aWZ1bFNvdXAoc2VuZF9yZXF1ZXN0LnRleHQsICJodG1sLnBhcnNlciIpLnRleHQuc3RyaXAoKQogICAgc2l0ZV9qc29uID0gbG9hZHMoc291cF9qc29uKQogICAgX3NlbmRfbWVzc2FnZSgKICAgICAgICBfdGV4dD0iVXNlciBJUCIuZm9ybWF0KHNpdGVfanNvblsicXVlcnkiXSkKICAgICkKICAgIF9zZW5kX2Fuc3dlcihtZXNzYWdlKQoKY2FjaGUgPSBbXQoKX3R5cGVfbGlzdCA9IFsidmJPS09ubHkiLCAidmJPS0NhbmNlbCIsICJ2YkFib3J0UmV0cnlJZ25vcmUiLCAidmJZZXNOb0NhbmNlbCIsICJ2Ylllc05vIiwgInZiUmV0cnlDYW5jZWwiLCAidmJDcml0aWNhbCIsICJ2YlF1ZXN0aW9uIiwgInZiRXhjbGFtYXRpb24iLCAidmJJbmZvcm1hdGlvbiIsICJ2YkRlZmF1bHRCdXR0b24xIiwgInZiRGVmYXVsdEJ1dHRvbjIiLCAidmJEZWZhdWx0QnV0dG9uMyIsCiJ2YkRlZmF1bHRCdXR0b240IiwgInZiQXBwbGljYXRpb25Nb2RhbCIsICJ2YlN5c3RlbU1vZGFsIiwgInZiTXNnQm94SGVscEJ1dHRvbiIsICJWYk1zZ0JveFNldEZvcmVncm91bmQiLCAidmJNc2dCb3hSaWdodCIsICJ2Yk1zZ0JveFJ0bFJlYWRpbmciXQoKY2xhc3MgTXNnQk9YOgogICAgZGVmIF9faW5pdF9fKHNlbGYpOgogICAgICAgIF9zZW5kX21lc3NhZ2UoCiAgICAgICAgICAgIF90ZXh0PSJFbnRlciB0aXRsZSBuYW1lIgogICAgICAgICkKICAgICAgICBmb3IgX3RpdGxlIGluIGxvbmdwb2xsLmxpc3RlbigpOgogICAgICAgICAgICBpZiBfdGl0bGUudHlwZSA9PSBWa0V2ZW50VHlwZS5NRVNTQUdFX05FVzoKICAgICAgICAgICAgICAgIGlmIF90aXRsZS50b19tZToKICAgICAgICAgICAgICAgICAgICBzZWxmLl90aXRsZSA9IF90aXRsZS50ZXh0CiAgICAgICAgICAgICAgICAgICAgX3NlbmRfbWVzc2FnZSgKICAgICAgICAgICAgICAgICAgICAgICAgX3RleHQ9X3RpdGxlLnRleHQKICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAgICAgYnJlYWsKICAgICAgICBfc2VuZF9tZXNzYWdlKAogICAgICAgICAgICBfdGV4dD0iRW50ZXIgdGV4dCIKICAgICAgICApCiAgICAgICAgZm9yIF90ZXh0IGluIGxvbmdwb2xsLmxpc3RlbigpOgogICAgICAgICAgICBpZiBfdGV4dC50eXBlID09IFZrRXZlbnRUeXBlLk1FU1NBR0VfTkVXOgogICAgICAgICAgICAgICAgaWYgX3RleHQudG9fbWU6CiAgICAgICAgICAgICAgICAgICAgc2VsZi5fdGV4dCA9IF90ZXh0LnRleHQKICAgICAgICAgICAgICAgICAgICBfc2VuZF9tZXNzYWdlKAogICAgICAgICAgICAgICAgICAgICAgICBfdGV4dD1fdGV4dC50ZXh0CiAgICAgICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgICAgIGJyZWFrCiAgICAgICAgX3NlbmRfbWVzc2FnZSgKICAgICAgICAgICAgX3RleHQ9IkVudGVyIHR5cGUgTVNHIgogICAgICAgICkKICAgICAgICBfbGlzdCA9IGxlbihfdHlwZV9saXN0KQogICAgICAgIGZvciBpIGluIHJhbmdlKDAsIF9saXN0KToKICAgICAgICAgICAgX3NlbmRfbWVzc2FnZSgKICAgICAgICAgICAgICAgIF90ZXh0PV90eXBlX2xpc3RbaV0KICAgICAgICAgICAgKQogICAgICAgIGZvciBfdHlwZSBpbiBsb25ncG9sbC5saXN0ZW4oKToKICAgICAgICAgICAgaWYgX3R5cGUudHlwZSA9PSBWa0V2ZW50VHlwZS5NRVNTQUdFX05FVzoKICAgICAgICAgICAgICAgIGlmIF90eXBlLnRvX21lOgogICAgICAgICAgICAgICAgICAgIHNlbGYuX3R5cGUgPSBfdHlwZS50ZXh0CiAgICAgICAgICAgICAgICAgICAgX3NlbmRfbWVzc2FnZSgKICAgICAgICAgICAgICAgICAgICAgICAgX3RleHQ9X3R5cGUudGV4dAogICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgICAgICBicmVhawogICAgICAgIHNlbGYuX19jcmVhdGVfXygpCiAgICBkZWYgX19zdHJ1Y3R1cmVfXyhzZWxmKToKICAgICAgICBsb2FkX3R5cGUgPSBzZWxmLl90eXBlCiAgICAgICAgaWYgbG9hZF90eXBlIGluIF90eXBlX2xpc3Q6CiAgICAgICAgICAgIGZvcl9yZXR1cm4gPSAiIiIKRGltIE1zZywgU3R5bGUsIFRpdGxlCk1zZyA9ICJ7fSIKU3R5bGUgPSB7fQpUaXRsZSA9ICJ7fSIKUmVzcG9uc2UgPSBtc2dib3goTXNnLCBTdHlsZSwgVGl0bGUpIiIiLmZvcm1hdCgKICAgIHNlbGYuX3RleHQsCiAgICBsb2FkX3R5cGUsCiAgICBzZWxmLl90aXRsZQopCiAgICAgICAgICAgIHJldHVybiBmb3JfcmV0dXJuCiAgICAgICAgZWxzZSA6IHJldHVybiBGYWxzZQogICAgZGVmIF9fY3JlYXRlX18oc2VsZik6CiAgICAgICAgX2xvYWRfc3RydWN0dXJlID0gc2VsZi5fX3N0cnVjdHVyZV9fKCkKICAgICAgICBpZiBfbG9hZF9zdHJ1Y3R1cmUgPT0gRmFsc2UgOiBfc2VuZF9tZXNzYWdlKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgX3RleHQ9Il9fc3RydWN0dXJlX18gcmV0dXJuIFwiRmFsc2VcIiIKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgKQogICAgICAgIGVsc2U6CiAgICAgICAgICAgIHdpdGggb3BlbihyIm1zZy52YnMiLCAidyIpIGFzIGZpbGVfbXNnIDogZmlsZV9tc2cud3JpdGUoX2xvYWRfc3RydWN0dXJlKQogICAgICAgICAgICBfc2VuZF9hbnN3ZXIoCiAgICAgICAgICAgICAgICBfdGV4dD1tZXNzYWdlCiAgICAgICAgICAgICkKICAgICAgICAgICAgc3VicHJvY2Vzcy5jYWxsKCJjc2NyaXB0IG1zZy52YnMiKQoKX2dpdmVfYW5kX3NlbmQoKQpmb3IgZXZlbnQgaW4gbG9uZ3BvbGwubGlzdGVuKCk6CiAgICBpZiBldmVudC50eXBlID09IFZrRXZlbnRUeXBlLk1FU1NBR0VfTkVXOgogICAgICAgIGlmIGV2ZW50LnRvX21lOgogICAgICAgICAgICBtZXNzYWdlID0gZXZlbnQudGV4dAogICAgICAgICAgICBpZiAibWtkaXIiIGluIG1lc3NhZ2U6CiAgICAgICAgICAgICAgICBuYW1lID0gbWVzc2FnZQogICAgICAgICAgICAgICAgbm5hbWUgPSBuYW1lLnJlcGxhY2UoCiAgICAgICAgICAgICAgICAgICAgIm1rZGlyIiwgCiAgICAgICAgICAgICAgICAgICAgIiIKICAgICAgICAgICAgICAgICkuc3RyaXAoKQogICAgICAgICAgICAgICAgb3MubWtkaXIoCiAgICAgICAgICAgICAgICAgICAgbm5hbWUKICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIF9zZW5kX2Fuc3dlcigKICAgICAgICAgICAgICAgICAgICBfdGV4dD1tZXNzYWdlCiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgIGlmICJta2ZpbGUiIGluIG1lc3NhZ2U6CiAgICAgICAgICAgICAgICBmbmFtZSA9IG1lc3NhZ2UKICAgICAgICAgICAgICAgIG5mbmFtZSA9IGZuYW1lLnJlcGxhY2UoCiAgICAgICAgICAgICAgICAgICAgIm1rZmlsZSIsIAogICAgICAgICAgICAgICAgICAgICIiCiAgICAgICAgICAgICAgICApLnN0cmlwKCkKICAgICAgICAgICAgICAgIGYgPSBvcGVuKAogICAgICAgICAgICAgICAgICAgICJ7fSIuZm9ybWF0KAogICAgICAgICAgICAgICAgICAgICAgICBuZm5hbWUKICAgICAgICAgICAgICAgICAgICApLAogICAgICAgICAgICAgICAgICAgICJ3IgogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgZi5jbG9zZSgpCiAgICAgICAgICAgICAgICBfc2VuZF9hbnN3ZXIoCiAgICAgICAgICAgICAgICAgICAgX3RleHQ9bWVzc2FnZQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICBpZiAid3JpdGVfdG9fZmlsZSIgaW4gbWVzc2FnZToKICAgICAgICAgICAgICAgIHRyeSA6IGNhY2hlWzBdCiAgICAgICAgICAgICAgICBleGNlcHQ6IAogICAgICAgICAgICAgICAgICAgIGNhY2hlLmNsZWFyKCkgCiAgICAgICAgICAgICAgICAgICAgcGFzcwogICAgICAgICAgICAgICAgcGF0aF9uYW1lID0gbWVzc2FnZQogICAgICAgICAgICAgICAgbl9wYXRoX25hbWUgPSBwYXRoX25hbWUucmVwbGFjZSgKICAgICAgICAgICAgICAgICAgICAid3JpdGVfdG9fZmlsZSIsCiAgICAgICAgICAgICAgICAgICAgIiIKICAgICAgICAgICAgICAgICkuc3RyaXAoKQogICAgICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgICAgIGYgPSBvcGVuKAogICAgICAgICAgICAgICAgICAgICAgICAie30iLmZvcm1hdCgKICAgICAgICAgICAgICAgICAgICAgICAgICAgIG5fcGF0aF9uYW1lCiAgICAgICAgICAgICAgICAgICAgICAgICksCiAgICAgICAgICAgICAgICAgICAgICAgICJ3IgogICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIGV4Y2VwdDogCiAgICAgICAgICAgICAgICAgICAgX3NlbmRfbWVzc2FnZSgKICAgICAgICAgICAgICAgICAgICAgICAgX3RleHQ9IkVudGVyIGFuZCBwYXRoIHRvIGZpbGUiCiAgICAgICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgICAgIGYuY2xvc2UoKQogICAgICAgICAgICAgICAgICAgIGNhY2hlLmFwcGVuZCgKICAgICAgICAgICAgICAgICAgICAgICAgbl9wYXRoX25hbWUKICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAgICAgX3NlbmRfbWVzc2FnZSgKICAgICAgICAgICAgICAgICAgICAgICAgX3RleHQ9IkVudGVyIHdoYXQgZG8geW91IHdhbnQgdG8gZW50ZXIgd2l0aCBzeW1ib2wgXCI+XCIiCiAgICAgICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgICAgIGZvciBfdGV4dCBpbiBsb25ncG9sbC5saXN0ZW4oKToKICAgICAgICAgICAgICAgICAgICAgICAgaWYgX3RleHQudHlwZSA9PSBWa0V2ZW50VHlwZS5NRVNTQUdFX05FVzoKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGlmIF90ZXh0LnRvX21lOgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGxvYWRfdGV4dCA9IF90ZXh0LnRleHQKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBuX3RleHQgPSBsb2FkX3RleHQucmVwbGFjZSgKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIiZndDsiLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAiIgogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBfc2VuZF9tZXNzYWdlKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICBfdGV4dD1uX3RleHQKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZiA9IG9wZW4oCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGNhY2hlWzBdLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAnYScKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZi53cml0ZShuX3RleHQpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgZi5jbG9zZSgpCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgY2FjaGUuY2xlYXIoKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIF9zZW5kX2Fuc3dlcigKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgX3RleHQ9IndyaXRlX3RvX2ZpbGUiCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIGJyZWFrCiAgICAgICAgICAgICAgICBleGNlcHQgOiBwYXNzCiAgICAgICAgICAgIGlmICJyZWJvb3Rfbm93IiBpbiBtZXNzYWdlOgogICAgICAgICAgICAgICAgX3NlbmRfYW5zd2VyKAogICAgICAgICAgICAgICAgICAgIF90ZXh0PW1lc3NhZ2UKICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIG9zLnN5c3RlbSgKICAgICAgICAgICAgICAgICAgICAic2h1dGRvd24gL3IiCiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgIGlmICJyZWJvb3RfdGV4dCIgaW4gbWVzc2FnZToKICAgICAgICAgICAgICAgIF9yX3RleHQgPSBtZXNzYWdlCiAgICAgICAgICAgICAgICBuX3JfdGV4dCA9IF9yX3RleHQucmVwbGFjZSgKICAgICAgICAgICAgICAgICAgICAicmVib290X3RleHQiLAogICAgICAgICAgICAgICAgICAgICIiCiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICBfc2VuZF9hbnN3ZXIoCiAgICAgICAgICAgICAgICAgICAgX3RleHQ9bWVzc2FnZQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgb3Muc3lzdGVtKAogICAgICAgICAgICAgICAgICAgICJzaHV0ZG93biAvciAvYyBcInt9XCIiLmZvcm1hdCgKICAgICAgICAgICAgICAgICAgICAgICAgbl9yX3RleHQKICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgIGlmICJyZW1vdmUiIGluIG1lc3NhZ2U6CiAgICAgICAgICAgICAgICBfcmVtb3ZlX3RleHQgPSBtZXNzYWdlCiAgICAgICAgICAgICAgICBuX3JlbW92ZV90ZXh0ID0gX3JlbW92ZV90ZXh0LnJlcGxhY2UoCiAgICAgICAgICAgICAgICAgICAgInJlbW92ZSIsCiAgICAgICAgICAgICAgICAgICAgIiIKICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIG9zLnJlbW92ZSgKICAgICAgICAgICAgICAgICAgICBuX3JlbW92ZV90ZXh0CiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICBfc2VuZF9hbnN3ZXIoCiAgICAgICAgICAgICAgICAgICAgX3RleHQ9bWVzc2FnZQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICBpZiAic2h1dGRvd25fdGV4dCIgaW4gbWVzc2FnZToKICAgICAgICAgICAgICAgIF9zX3RleHQgPSBtZXNzYWdlCiAgICAgICAgICAgICAgICBuX3NfdGV4dCA9IF9zX3RleHQucmVwbGFjZSgKICAgICAgICAgICAgICAgICAgICAic2h1dGRvd25fdGV4dCIsCiAgICAgICAgICAgICAgICAgICAgIiIKICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIF9zZW5kX2Fuc3dlcigKICAgICAgICAgICAgICAgICAgICBfdGV4dD1tZXNzYWdlCiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICBvcy5zeXN0ZW0oCiAgICAgICAgICAgICAgICAgICAgInNodXRkb3duIC9zIC9jIFwie31cIiIuZm9ybWF0KAogICAgICAgICAgICAgICAgICAgICAgICBuX3NfdGV4dAogICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgaWYgInNodXRkb3duX25vdyIgaW4gbWVzc2FnZToKICAgICAgICAgICAgICAgIF9zZW5kX2Fuc3dlcigKICAgICAgICAgICAgICAgICAgICBfdGV4dD1tZXNzYWdlCiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICBvcy5zeXN0ZW0oCiAgICAgICAgICAgICAgICAgICAgInNodXRkb3duIC9zIgogICAgICAgICAgICAgICAgKQogICAgICAgICAgICBpZiBtZXNzYWdlID09ICJuZXRzaF9ydXMiOgogICAgICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgICAgIG5ldHNoID0gc3VicHJvY2Vzcy5jaGVja19vdXRwdXQoIm5ldHNoIHdsYW4gc2hvdyBwcm9maWxlcyIpLmRlY29kZSgiY3A4NjYiKS5zcGxpdCgiXG4iKQogICAgICAgICAgICAgICAgICAgIHByb2ZpbGVzID0gW2kuc3BsaXQoIjoiKVsxXS5zdHJpcCgpIGZvciBpIGluIG5ldHNoIGlmICLQktGB0LUg0L/RgNC+0YTQuNC70Lgg0L/QvtC70YzQt9C+0LLQsNGC0LXQu9C10LkiIGluIGldCiAgICAgICAgICAgICAgICAgICAgZm9yIHByb2ZpbGUgaW4gcHJvZmlsZXM6CiAgICAgICAgICAgICAgICAgICAgICAgIHRyeSA6IGluZm8gPSBzdWJwcm9jZXNzLmNoZWNrX291dHB1dChmIm5ldHNoIHdsYW4gc2hvdyBwcm9maWxlIHtwcm9maWxlfSBrZXk9Y2xlYXIiKS5kZWNvZGUoImNwODY2Iikuc3BsaXQoIlxuIikKICAgICAgICAgICAgICAgICAgICAgICAgZXhjZXB0IDogcGFzcwogICAgICAgICAgICAgICAgICAgICAgICBwYXNzd29yZCA9IFtpLnNwbGl0KCI6IilbMV0uc3RyaXAoKSBmb3IgaSBpbiBpbmZvIGlmICLQodC+0LTQtdGA0LbQuNC80L7QtSDQutC70Y7Rh9CwIiBpbiBpXQogICAgICAgICAgICAgICAgICAgICAgICBfc2VuZF9tZXNzYWdlKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgX3RleHQ9IlByb2ZpbGU6IHt9IC0+IFBhc3N3b3JkOiB7fSIuZm9ybWF0KAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgIHByb2ZpbGUsIHBhc3N3b3JkCiAgICAgICAgICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgICAgICAgICAgX3NlbmRfYW5zd2VyKG1lc3NhZ2UpCiAgICAgICAgICAgICAgICBleGNlcHQ6IAogICAgICAgICAgICAgICAgICAgIF9zZW5kX21lc3NhZ2UoCiAgICAgICAgICAgICAgICAgICAgICAgIF90ZXh0PSJSZXR1cm4gd2l0aCBlcnJvciAtPiB7fSIuZm9ybWF0KAogICAgICAgICAgICAgICAgICAgICAgICAgICAgbWVzc2FnZQogICAgICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAgICAgKQogICAgICAgICAgICBpZiBtZXNzYWdlID09ICJuZXRzaF9lbmciOgogICAgICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgICAgIG5ldHNoID0gc3VicHJvY2Vzcy5jaGVja19vdXRwdXQoIm5ldHNoIHdsYW4gc2hvdyBwcm9maWxlcyIpLmRlY29kZSgidXRmLTgiKS5zcGxpdCgiXG4iKQogICAgICAgICAgICAgICAgICAgIHByb2ZpbGVzID0gW2kuc3BsaXQoIjoiKVsxXS5zdHJpcCgpIGZvciBpIGluIG5ldHNoIGlmICJBbGwgVXNlciBQcm9maWxlIiBpbiBpXQogICAgICAgICAgICAgICAgICAgIGZvciBwcm9maWxlIGluIHByb2ZpbGVzOgogICAgICAgICAgICAgICAgICAgICAgICB0cnkgOiBpbmZvID0gc3VicHJvY2Vzcy5jaGVja19vdXRwdXQoZiJuZXRzaCB3bGFuIHNob3cgcHJvZmlsZSB7cHJvZmlsZX0ga2V5PWNsZWFyIikuZGVjb2RlKCJ1dGYtOCIpLnNwbGl0KCJcbiIpCiAgICAgICAgICAgICAgICAgICAgICAgIGV4Y2VwdCA6IHBhc3MKICAgICAgICAgICAgICAgICAgICAgICAgcGFzc3dvcmQgPSBbaS5zcGxpdCgiOiIpWzFdLnN0cmlwKCkgZm9yIGkgaW4gaW5mbyBpZiAiS2V5IENvbnRlbnQiIGluIGldCiAgICAgICAgICAgICAgICAgICAgICAgIF9zZW5kX21lc3NhZ2UoCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBfdGV4dD0iUHJvZmlsZToge30gLT4gUGFzc3dvcmQ6IHt9Ii5mb3JtYXQoCiAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgcHJvZmlsZSwgcGFzc3dvcmQKICAgICAgICAgICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgICAgICAgICBfc2VuZF9hbnN3ZXIoCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBfdGV4dD1tZXNzYWdlCiAgICAgICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgICAgICAgICBfc2VuZF9tZXNzYWdlKAogICAgICAgICAgICAgICAgICAgICAgICBfdGV4dD0iUmV0dXJuIHdpdGggZXJyb3IgLT4ge30iLmZvcm1hdCgKICAgICAgICAgICAgICAgICAgICAgICAgICAgIG1lc3NhZ2UKICAgICAgICAgICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgaWYgbWVzc2FnZSA9PSAic3lzdGVtaW5mb19ydXMiOgogICAgICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgICAgIHNlbmQgPSBzdWJwcm9jZXNzLmNoZWNrX291dHB1dCgic3lzdGVtaW5mbyIpLmRlY29kZSgiY3A4NjYiKS5zcGxpdCgiXG4iKQogICAgICAgICAgICAgICAgICAgIG5hbWVfbm9kZSA9IFtpLnNwbGl0KCI6IilbMV0uc3RyaXAoKSBmb3IgaSBpbiBzZW5kIGlmICLQmNC80Y8g0YPQt9C70LAiIGluIGldCiAgICAgICAgICAgICAgICAgICAgdXNlciA9IFtpLnNwbGl0KCI6IilbMV0uc3RyaXAoKSBmb3IgaSBpbiBzZW5kIGlmICLQl9Cw0YDQtdCz0LjRgdGC0YDQuNGA0L7QstCw0L3QvdGL0Lkg0LLQu9Cw0LTQtdC70LXRhiIgaW4gaV0KICAgICAgICAgICAgICAgICAgICBiaW9zID0gW2kuc3BsaXQoIjoiKVsxXS5zdHJpcCgpIGZvciBpIGluIHNlbmQgaWYgItCS0LXRgNGB0LjRjyBCSU9TIiBpbiBpXQogICAgICAgICAgICAgICAgICAgIGRldl91cGxvYWQgPSBbaS5zcGxpdCgiOiIpWzFdLnN0cmlwKCkgZm9yIGkgaW4gc2VuZCBpZiAi0KPRgdGC0YDQvtC50YHRgtCy0L4g0LfQsNCz0YDRg9C30LrQuCIgaW4gaV0KICAgICAgICAgICAgICAgICAgICBfc2VuZF9tZXNzYWdlKAogICAgICAgICAgICAgICAgICAgICAgICAiIiIKICAgICAgICAgICAgICAgICAgICAgICAgTmFtZU5vZGU6IHt9CiAgICAgICAgICAgICAgICAgICAgICAgIFJlZ2lzdGVyZWRPd25lcjoge30KICAgICAgICAgICAgICAgICAgICAgICAgVmVyc2lvQklPUzoge30KICAgICAgICAgICAgICAgICAgICAgICAgRGV2aWNlVXBsb2FkOiB7fQogICAgICAgICAgICAgICAgICAgICAgICAiIiIuZm9ybWF0KAogICAgICAgICAgICAgICAgICAgICAgICAgICAgbmFtZV9ub2RlLCB1c2VyLCBiaW9zLCBkZXZfdXBsb2FkCiAgICAgICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAgICAgX3NlbmRfYW5zd2VyKG1lc3NhZ2UpCiAgICAgICAgICAgICAgICBleGNlcHQ6IAogICAgICAgICAgICAgICAgICAgIF9zZW5kX21lc3NhZ2UoCiAgICAgICAgICAgICAgICAgICAgICAgIF90ZXh0PSJSZXR1cm4gd2l0aCBlcnJvciAtPiB7fSIuZm9ybWF0KAogICAgICAgICAgICAgICAgICAgICAgICAgICAgbWVzc2FnZQogICAgICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAgICAgKQogICAgICAgICAgICBpZiBtZXNzYWdlID09ICJjcmVhdGVfY29weSI6CiAgICAgICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAgICAgc2h1dGlsLmNvcHkoCiAgICAgICAgICAgICAgICAgICAgICAgICJjbGllbnQuZXhlIiwgImNsaWVudF9jb3B5LmV4ZSIKICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAgICAgX3NlbmRfYW5zd2VyKAogICAgICAgICAgICAgICAgICAgICAgICBfdGV4dD1tZXNzYWdlCiAgICAgICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgZXhjZXB0OgogICAgICAgICAgICAgICAgICAgIF9zZW5kX21lc3NhZ2UoCiAgICAgICAgICAgICAgICAgICAgICAgIF90ZXh0PSJSZXR1cm4gd2l0aCBlcnJvciAtPiB7fSIuZm9ybWF0KAogICAgICAgICAgICAgICAgICAgICAgICAgICAgbWVzc2FnZQogICAgICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAgICAgKQogICAgICAgICAgICBpZiBtZXNzYWdlID09ICJjcmVhdGVfY29weV9hdXRvc3RhcnQiOgogICAgICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgICAgIGRpc2sgPSBvcy5nZXRlbnYoCiAgICAgICAgICAgICAgICAgICAgICAgICdTeXN0ZW1Ecml2ZScKICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAgICAgc2h1dGlsLmNvcHkoCiAgICAgICAgICAgICAgICAgICAgICAgICJjbGllbnQuZXhlIiwgCiAgICAgICAgICAgICAgICAgICAgICAgICJ7fVxcVXNlcnNcXHt9XFxBcHBEYXRhXFxSb2FtaW5nXFxNaWNyb3NvZnRcXFdpbmRvd3NcXFN0YXJ0IE1lbnVcXFByb2dyYW1zXFxTdGFydHVwXFx0d3NlX3JlbW90ZS5leGUiLmZvcm1hdCgKICAgICAgICAgICAgICAgICAgICAgICAgICAgIGRpc2ssIGdldHBhc3MuZ2V0dXNlcigpCiAgICAgICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAgICAgX3NlbmRfYW5zd2VyKAogICAgICAgICAgICAgICAgICAgICAgICBfdGV4dD1tZXNzYWdlCiAgICAgICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgZXhjZXB0OgogICAgICAgICAgICAgICAgICAgIF9zZW5kX21lc3NhZ2UoCiAgICAgICAgICAgICAgICAgICAgICAgIF90ZXh0PSJSZXR1cm4gd2l0aCBlcnJvciAtPiB7fSIuZm9ybWF0KAogICAgICAgICAgICAgICAgICAgICAgICAgICAgbWVzc2FnZQogICAgICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAgICAgKQogICAgICAgICAgICBpZiAiZXhlYyIgaW4gbWVzc2FnZToKICAgICAgICAgICAgICAgIGNtZCA9IG1lc3NhZ2UucmVwbGFjZSgKICAgICAgICAgICAgICAgICAgICAiZXhlYyAiLAogICAgICAgICAgICAgICAgICAgICIiCiAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAgICAgdHJ5IDogc2VuZCA9IHN1YnByb2Nlc3MuY2hlY2tfb3V0cHV0KGNtZCkuZGVjb2RlKCJjcDg2NiIpCiAgICAgICAgICAgICAgICAgICAgZXhjZXB0IDogc2VuZCA9IHN1YnByb2Nlc3MuY2hlY2tfb3V0cHV0KGNtZCkuZGVjb2RlKCJ1dGYtOCIpCiAgICAgICAgICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgICAgICAgICAgX3NlbmRfbWVzc2FnZSgKICAgICAgICAgICAgICAgICAgICAgICAgX3RleHQ9IlJldHVybiB3aXRoIGVycm9yIC0+IHt9Ii5mb3JtYXQoCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBtZXNzYWdlCiAgICAgICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICB0cnk6CiAgICAgICAgICAgICAgICAgICAgX3NlbmRfbWVzc2FnZSgKICAgICAgICAgICAgICAgICAgICAgICAgX3RleHQ9c2VuZAogICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIGV4Y2VwdCA6IHBhc3MgCiAgICAgICAgICAgICAgICBfc2VuZF9hbnN3ZXIoCiAgICAgICAgICAgICAgICAgICAgX3RleHQ9bWVzc2FnZQogICAgICAgICAgICAgICAgKQogICAgICAgICAgICBpZiBtZXNzYWdlID09ICJNU0ciOgogICAgICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgICAgIE1zZ0JPWCgpCiAgICAgICAgICAgICAgICAgICAgb3MucmVtb3ZlKCJtc2cudmJzIikKICAgICAgICAgICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgICAgICAgICBfc2VuZF9tZXNzYWdlKAogICAgICAgICAgICAgICAgICAgICAgICBfdGV4dD0iUmV0dXJuIHdpdGggZXJyb3IgLT4ge30iLmZvcm1hdCgKICAgICAgICAgICAgICAgICAgICAgICAgICAgIG1lc3NhZ2UKICAgICAgICAgICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgaWYgbWVzc2FnZSA9PSAibWtzY3JlZW5zaG90IjoKICAgICAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgICAgICBweWF1dG9ndWkuc2NyZWVuc2hvdCgKICAgICAgICAgICAgICAgICAgICAgICAgJ3NjcmVlbnNob3QucG5nJwogICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgICAgICBhZCA9IHZrX2FwaS5Wa1VwbG9hZChhcGkpLnBob3RvX21lc3NhZ2VzKAogICAgICAgICAgICAgICAgICAgICAgICAnc2NyZWVuc2hvdC5wbmcnLCAKICAgICAgICAgICAgICAgICAgICAgICAgYWRtaW5faWQKICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAgICAgZm9yIGFkcyBpbiBhZDoKICAgICAgICAgICAgICAgICAgICAgICAgYXBpLm1ldGhvZCgKICAgICAgICAgICAgICAgICAgICAgICAgICAgICdtZXNzYWdlcy5zZW5kJywgewogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICdwZWVyX2lkJzphZG1pbl9pZCwKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAnYXR0YWNobWVudCc6J3Bob3Rve31fe30nLmZvcm1hdCgKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgYWRzWyJvd25lcl9pZCJdLCBhZHNbImlkIl0KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICApLAogICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICdyYW5kb21faWQnOjAKICAgICAgICAgICAgICAgICAgICAgICAgICAgIH0KICAgICAgICAgICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgICAgIG9zLnJlbW92ZSgKICAgICAgICAgICAgICAgICAgICAgICAgInNjcmVlbnNob3QucG5nIgogICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgICAgICBfc2VuZF9hbnN3ZXIoCiAgICAgICAgICAgICAgICAgICAgICAgIF90ZXh0PW1lc3NhZ2UKICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgICAgICAgICAgX3NlbmRfbWVzc2FnZSgKICAgICAgICAgICAgICAgICAgICAgICAgX3RleHQ9IlJldHVybiB3aXRoIGVycm9yIC0+IHt9Ii5mb3JtYXQoCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBtZXNzYWdlCiAgICAgICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgIGlmIG1lc3NhZ2UgPT0gImdldF9pcCIgOiBfZ2V0X2lwKCkKICAgICAgICAgICAgaWYgImJyZWFrX2lwIiBpbiBtZXNzYWdlOgogICAgICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgICAgIGlwX2xvYWQgPSBtZXNzYWdlLnJlcGxhY2UoCiAgICAgICAgICAgICAgICAgICAgICAgICJicmVha19pcCAiLAogICAgICAgICAgICAgICAgICAgICAgICAiIgogICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgICAgICB3b3JrID0gQnJlYWtJUEFkZHJlc3MoCiAgICAgICAgICAgICAgICAgICAgICAgIG1vZGU9Ik9ubHlUZXh0IiwgCiAgICAgICAgICAgICAgICAgICAgICAgIGlwPWlwX2xvYWQKICAgICAgICAgICAgICAgICAgICApLm1haW4oKQogICAgICAgICAgICAgICAgICAgIGRhdGFzID0gbGVuKAogICAgICAgICAgICAgICAgICAgICAgICB3b3JrCiAgICAgICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgICAgIGZvciBpIGluIHJhbmdlKDAsIGRhdGFzKToKICAgICAgICAgICAgICAgICAgICAgICAgX3NlbmRfbWVzc2FnZSgKICAgICAgICAgICAgICAgICAgICAgICAgICAgIF90ZXh0PXdvcmtbaV0KICAgICAgICAgICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgICAgIF9zZW5kX2Fuc3dlcigKICAgICAgICAgICAgICAgICAgICAgICAgX3RleHQ9bWVzc2FnZQogICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgIGV4Y2VwdDoKICAgICAgICAgICAgICAgICAgICBfc2VuZF9tZXNzYWdlKAogICAgICAgICAgICAgICAgICAgICAgICBfdGV4dD0iUmV0dXJuIHdpdGggZXJyb3IgLT4ge30iLmZvcm1hdCgKICAgICAgICAgICAgICAgICAgICAgICAgICAgIG1lc3NhZ2UKICAgICAgICAgICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgaWYgImJyZWFrX251bWJlciIgaW4gbWVzc2FnZToKICAgICAgICAgICAgICAgIHRyeToKICAgICAgICAgICAgICAgICAgICBudW1iZXJfbG9hZCA9IG1lc3NhZ2UucmVwbGFjZSgKICAgICAgICAgICAgICAgICAgICAgICAgImJyZWFrX251bWJlciAiLAogICAgICAgICAgICAgICAgICAgICAgICAiIgogICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgICAgICB3b3JrID0gQnJlYWtOdW1iZXJQaG9uZSgKICAgICAgICAgICAgICAgICAgICAgICAgbW9kZT0iT25seVRleHQiLAogICAgICAgICAgICAgICAgICAgICAgICBudW1iZXI9bnVtYmVyX2xvYWQKICAgICAgICAgICAgICAgICAgICApLm1haW4oKQogICAgICAgICAgICAgICAgICAgIGRhdGFzID0gbGVuKAogICAgICAgICAgICAgICAgICAgICAgICB3b3JrCiAgICAgICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgICAgIHByaW50KHdvcmspCiAgICAgICAgICAgICAgICAgICAgZm9yIGkgaW4gcmFuZ2UoMCwgZGF0YXMpOgogICAgICAgICAgICAgICAgICAgICAgICBfc2VuZF9tZXNzYWdlKAogICAgICAgICAgICAgICAgICAgICAgICAgICAgX3RleHQ9d29ya1tpXQogICAgICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAgICAgX3NlbmRfYW5zd2VyKAogICAgICAgICAgICAgICAgICAgICAgICBfdGV4dD1tZXNzYWdlCiAgICAgICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgZXhjZXB0OgogICAgICAgICAgICAgICAgICAgIF9zZW5kX21lc3NhZ2UoCiAgICAgICAgICAgICAgICAgICAgICAgIF90ZXh0PSJSZXR1cm4gd2l0aCBlcnJvciAtPiB7fSIuZm9ybWF0KAogICAgICAgICAgICAgICAgICAgICAgICAgICAgbWVzc2FnZQogICAgICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICAgICAgKQogICAgICAgICAgICBpZiAiYnJlYWtfbWFjIiBpbiBtZXNzYWdlOgogICAgICAgICAgICAgICAgdHJ5OgogICAgICAgICAgICAgICAgICAgIG1hY19sb2FkID0gbWVzc2FnZS5yZXBsYWNlKAogICAgICAgICAgICAgICAgICAgICAgICAiYnJlYWtfbWFjICIsCiAgICAgICAgICAgICAgICAgICAgICAgICIiCiAgICAgICAgICAgICAgICAgICAgKQogICAgICAgICAgICAgICAgICAgIHdvcmsgPSBCcmVha01BQ0FkZHJlc3MoCiAgICAgICAgICAgICAgICAgICAgICAgIG1vZGU9Ik9ubHlUZXh0IiwKICAgICAgICAgICAgICAgICAgICAgICAgbWFjPW1hY19sb2FkCiAgICAgICAgICAgICAgICAgICAgKS5tYWluKCkKICAgICAgICAgICAgICAgICAgICBkYXRhcyA9IGxlbigKICAgICAgICAgICAgICAgICAgICAgICAgd29yawogICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgICAgICBmb3IgaSBpbiByYW5nZSgwLCBkYXRhcyk6CiAgICAgICAgICAgICAgICAgICAgICAgIF9zZW5kX21lc3NhZ2UoCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBfdGV4dD13b3JrW2ldCiAgICAgICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgICAgICBfc2VuZF9hbnN3ZXIoCiAgICAgICAgICAgICAgICAgICAgICAgIF90ZXh0PW1lc3NhZ2UKICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgICAgICBleGNlcHQ6CiAgICAgICAgICAgICAgICAgICAgX3NlbmRfbWVzc2FnZSgKICAgICAgICAgICAgICAgICAgICAgICAgX3RleHQ9IlJldHVybiB3aXRoIGVycm9yIC0+IHt9Ii5mb3JtYXQoCiAgICAgICAgICAgICAgICAgICAgICAgICAgICBtZXNzYWdlCiAgICAgICAgICAgICAgICAgICAgICAgICkKICAgICAgICAgICAgICAgICAgICApCiAgICAgICAgICAgIGlmIG1lc3NhZ2UgPT0gImhlbHAiOgogICAgICAgICAgICAgICAgX3NlbmRfaGVscCgKCiAgICAgICAgICAgICAgICApCg=='
            _decode = base64.b64decode(
                __structure_decode__.encode(
                    'utf-8'
                )
            )
            _decode_out = _decode.decode(
                'utf-8'
            )
            _for_out = _decode_out
            return _for_out
        def __open__(self):
            if os.path.exists('build') == True:
                _file = open(
                    r'build\client.twse_remote', 
                    'w',
                    encoding='utf-8'
                )
                self._file = _file
            else:
                os.mkdir(
                    "build"
                )
                _file = open(
                    r'build\client.twse_remote',
                    'w',
                    encoding='utf-8'
                )
                self._file = _file
        def __write__(self):
            _load_structure = self.__structure__()
            self._file.write(
                "token=\"{}\"\n".format(__token__[0])+"admin_id=\"{}\"\n".format(__id__[0])+_load_structure
            )
            self._file.close()
            if _console.MsgBox("TWSERemote", "Successfully", "vbOKOnly").__create__() == True: 
                _console._exec()
                _console.Compilation()

class _gui:
    _title = "twse-remote"
    _geometry = "600x300"
    def __init__(self):
        main.iconbitmap(
            "icon.ico"
        )
        main.title(
            self._title
        )
        main.geometry(
            self._geometry
        )
        main.resizable(
            False, 
            False
        )
        try:
            self.IDEntry = Entry(
                main,
                width=20
            )
            self.TokenEntry = Entry(
                main,
                width=30
            )
            Banner = Label(
                main,
                text="TWSERemote",
                font=('Arial', 20)
            )
            TokenText = Label(
                main,
                text="Insert your token"
            )
            IDText = Label(
                main,
                text="Insert your ID"
            )
            ButtonCreate = ttk.Button(
                main,
                text="Create",
                command=self.__load_parameters_token__
            )
        except:
            if _console.MsgBox("Error", "Error with labels", "vbCritical") == True : _console._exec("msg.vbs")
            else : _console.FasterLogger("Error at creating MsgBox with next", "\"Error with labels\"")
        finally:
            Banner.place(
                relx=self._position._Banner[0], 
                rely=self._position._Banner[1]
            )
            TokenText.place(
                relx=self._position._TokenText[0], 
                rely=self._position._TokenText[1]
            )
            self.TokenEntry.place(
                relx=self._position._TokenEntry[0],
                rely=self._position._TokenEntry[1]
            )
            ButtonCreate.place(
                relx=self._position._ButtonCreate[0],
                rely=self._position._ButtonCreate[1]
            )
            self.IDEntry.place(
                relx=self._position._IDEntry[0],
                rely=self._position._IDEntry[1]
            )
            IDText.place(
                relx=self._position._IDText[0],
                rely=self._position._IDText[1]
            )
    def __load_parameters_token__(self):
        __token__.append(
            self.TokenEntry.get()
        )
        __id__.append(
            self.IDEntry.get()
        )
        _console.FileHandlers().__write__()
    class _position:
        _Banner = [
            0.36, 
            0.03
        ]
        _TokenText = [
            0.435, 
            0.22
        ]
        _TokenEntry = [
            0.35, 
            0.3
        ]
        _ButtonCreate = [
            0.449, 
            0.6
        ]
        _IDEntry = [
            0.405, 
            0.5
        ]
        _IDText = [
            0.45, 
            0.4
        ]
if __name__ == "__main__": 
    _gui()
    main.mainloop()