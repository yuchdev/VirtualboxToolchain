from replace_pair import ReplacePair
from replace_content_tabs import REPLACE_CONTENT_TABS


__doc__ = """DO NOT REFORMAT THIS FILE
It is beinng merged below with REPLACE_CONTENT_TABS dict (see replace_content_tabs.py), 
which is formatted with tabs instead of spaces, to perform search-replace algorithm 
in tabs-formatted Virtualbox config files.
However, most of Virtualbox config files were formatted with spaces.
Do not change any formatting or layout of text within the patterns, 
because it would affect search-replace algorithm.
"""


REPLACE_CONTENT = {

    r"configure.vbs": [

        ReplacePair(
            old_text=r"""if Shell(DosSlashes(strPathVC & "/bin/cl.exe"), True) <> 0 then""",
            new_text=r"""if Shell(DosSlashes(strPathVC & "/bin/cl.exe") & " /?", True) <> 0 then"""
        ),

        ReplacePair(
            old_text=r"""   if   LogFileExists(strPathCurl, "include/curl/curl.h") _
    And LogFindFile(strPathCurl, "libcurl.dll") <> "" _
    And LogFindFile(strPathCurl, "libcurl.lib") <> "" _""",
            new_text=r"""if   LogFileExists(strPathCurl, "include/curl/curl.h") _
    And LogFindFile(strPathCurl, "libcurl.lib") <> "" _"""
        ),

        ReplacePair(
            old_text=r'''function CheckForPython(strPathPython)

   PrintHdr "Python"

   CheckForPython = False
   LogPrint "trying: strPathPython=" & strPathPython

   if LogFileExists(strPathPython, "python.exe") then
      CfgPrint "VBOX_BLD_PYTHON       := " & strPathPython & "\python.exe"
      CheckForPython = True
   end if

   PrintResult "Python ", strPathPython
end function''',
            new_text=r'''function CheckForPython(strPathPython)

   PrintHdr "Python"

   CheckForPython = False
   LogPrint "trying: strPathPython=" & strPathPython

   if LogFileExists(strPathPython, "python.exe") then
      CfgPrint "VBOX_BLD_PYTHON       := " & strPathPython & "/python.exe"
      CheckForPython = True
   end if

   PrintResult "Python ", strPathPython
end function

''
' Checks for libvpx
sub CheckForVpx(strOptVpx)
   dim strPathVpx, str
   strVpx = "libvpx"
   PrintHdr strVpx

   if strOptVpx = "" then
      MsgError "Invalid path specified!"
      exit sub
   end if

   if g_strTargetArch = "amd64" then
      strVsBuildArch = "x64"
   else
      strVsBuildArch = "Win32"
   end if
   strLibPathVpx = "lib/" & strVsBuildArch & "/vpxmd.lib"

   strPathVpx = ""
   if   LogFileExists(strOptVpx, "include/vpx/vpx_encoder.h") _
    And LogFileExists(strOptVpx, strLibPathVpx) _
      then
         strPathVpx = UnixSlashes(PathAbs(strOptVpx))
         CfgPrint "SDK_VBOX_VPX_INCS := " & strPathVpx & "/include"
         CfgPrint "SDK_VBOX_VPX_LIBS := " & strPathVpx & "/" & strLibPathVpx
      else
         MsgError "Can't locate " & strVpx & ". " _
                & "Please consult the configure.log and the build requirements."
         exit sub
      end if

   PrintResult strVpx, strPathVpx
end sub

''
' Checks for libopus
sub CheckForOpus(strOptOpus)
   dim strPathOpus, str
   strOpus = "libopus"
   PrintHdr strOpus

   if strOptOpus = "" then
      MsgError "Invalid path specified!"
      exit sub
   end if

   if g_strTargetArch = "amd64" then
      strVsBuildArch = "x64"
   else
      strVsBuildArch = "Win32"
   end if
   strLibPathOpus = "lib/" & strVsBuildArch & "/opus.lib"

   strPathOpus = ""
   if   LogFileExists(strOptOpus, "include/opus.h") _
    And LogFileExists(strOptOpus, strLibPathOpus) _
      then
         strPathOpus = UnixSlashes(PathAbs(strOptOpus))
         CfgPrint "SDK_VBOX_OPUS_INCS := " & strPathOpus & "/include"
         CfgPrint "SDK_VBOX_OPUS_LIBS := " & strPathOpus & "/" & strLibPathOpus
      else
         MsgError "Can't locate " & strOpus & ". " _
                & "Please consult the configure.log and the build requirements."
         exit sub
      end if

   PrintResult strOpus, strPathOpus
end sub'''
        ),

        ReplacePair(
            old_text=r'''   Print "  --with-python=PATH    "''',
            new_text=r'''   Print "  --with-python=PATH    "
   Print "  --with-libvpx=PATH    "
   Print "  --with-libopus=PATH   "'''
        ),

        ReplacePair(
            old_text=r'''   strOptPython = ""''',
            new_text=r'''   strOptPython = ""
   strOptVpx = ""
   strOptOpus = ""'''
        ),

        ReplacePair(
            old_text=r'''         case "--with-python"
            strOptPython = strPath''',
            new_text=r'''         case "--with-python"
            strOptPython = strPath
         case "--with-libvpx"
            strOptVpx = strPath
         case "--with-libopus"
            strOptOpus = strPath'''
        ),

        ReplacePair(
            old_text=r'''   if (strOptPython <> "") then
     CheckForPython strOptPython
   end if''',
            new_text=r'''   if (strOptPython <> "") then
     CheckForPython strOptPython
   end if
   if (strOptVpx <> "") then
     CheckForVpx strOptVpx
   end if
   if (strOptOpus <> "") then
     CheckForOpus strOptOpus
   end if'''
        )
    ],

    r"src\VBox\Runtime\r3\win\VBoxRT-openssl-1.1plus.def": [
        ReplacePair(
            old_text=r'''    ; tstRTBigNum.cpp
    BN_div
    BN_mul
    BN_mod_exp_simple
    BN_ucmp''',
            new_text=r'''    ; tstRTBigNum.cpp
    BN_div
    BN_mul
    BN_mod_exp_simple
    BN_ucmp

    ; VBoxRT.dll OpenSSL imports
    OpenSSL_version_num
    DH_generate_parameters_ex
    DH_new
    ASN1_STRING_get0_data'''
        )
    ],

    r"doc\manual\Makefile.kmk": [
        ReplacePair(
            old_text=r'''$$(VBOX_PATH_MANUAL_OUTBASE)/$(1)/user_$(2): $(3) \
		$$(VBOX_PATH_MANUAL_SRC)/docbook-refentry-to-manual-sect1.xsl \
		$$(VBOX_XML_CATALOG) $$(VBOX_XML_CATALOG_DOCBOOK) $$(VBOX_XML_CATALOG_MANUAL) \
		$$(VBOX_XML_ENTITIES) $$(VBOX_VERSION_STAMP) | $$$$(dir $$$$@)
	$$(call MSG_TOOL,xsltproc $$(notdir $$(filter %.xsl,$$^)),,$$(filter %.xml,$$^),$$@)
	$$(QUIET)$$(RM) -f "$$@"
	$$(QUIET)$$(call VBOX_XSLTPROC_WITH_CAT) --output $$@ $$(VBOX_PATH_MANUAL_SRC)/docbook-refentry-to-manual-sect1.xsl $$<''',
            new_text=r'''$$(VBOX_PATH_MANUAL_OUTBASE)/$(1)/user_$(2): $(3) \
		$$(VBOX_PATH_MANUAL_SRC)/docbook-refentry-to-manual-sect1.xsl \
		$$(VBOX_XML_CATALOG) $$(VBOX_XML_CATALOG_DOCBOOK) $$(VBOX_XML_CATALOG_MANUAL) \
		$$(VBOX_XML_ENTITIES) $$(VBOX_VERSION_STAMP) | $$$$(dir $$$$@)
	$$(call MSG_TOOL,xsltproc $$(notdir $$(filter %.xsl,$$^)),,$$(filter %.xml,$$^),$$@)
	$$(QUIET)$$(RM) -f "$$@"
	$$(QUIET)$$(MKDIR) -p "$$(@D)"
	$$(QUIET)$$(call VBOX_XSLTPROC_WITH_CAT) --output $$@ $$(VBOX_PATH_MANUAL_SRC)/docbook-refentry-to-manual-sect1.xsl $$<'''
        )
    ],

    r"doc\manual\Config.kmk": [

        ReplacePair(
            old_text=r''' VBOX_FILE_URL_MAYBE_SLASH = $(if $(eq $(KBUILD_HOST),win),/,)''',
            new_text=r''' VBOX_FILE_URL_MAYBE_SLASH = $(if $(eq $(KBUILD_HOST),win),/,)
 # Triple-slash for raw paths
 VBOX_PATH_MANUAL_SRC_SLASHED = $(subst :/,:///,$(VBOX_PATH_MANUAL_SRC))
 VBOX_PATH_MANUAL_OUTBASE_SLASHED = $(subst :/,:///,$(VBOX_PATH_MANUAL_OUTBASE))'''
        ),

        ReplacePair(
            old_text=r"""		'<catalog xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">' \
		'  <delegatePublic publicIdStartString="-//OASIS/ENTITIES DocBook XML"      catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_DOCBOOK)"/>' \
		'  <delegatePublic publicIdStartString="-//OASIS/DTD DocBook XML"           catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_DOCBOOK)"/>' \
		'  <delegateSystem systemIdStartString="http://www.oasis-open.org/docbook/" catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_DOCBOOK)"/>' \
		'  <delegateSystem systemIdStartString="http://docbook.org/"                catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_DOCBOOK)"/>' \
		'  <delegateURI uriStartString="http://www.oasis-open.org/docbook/"         catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_DOCBOOK)"/>' \
		'  <delegateURI uriStartString="http://docbook.org/"                        catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_DOCBOOK)"/>' \
		'  <delegateSystem systemIdStartString="$(VBOX_PATH_MANUAL_SRC)"            catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_MANUAL)"/>' \
		'  <delegateSystem systemIdStartString="$(VBOX_PATH_MANUAL_OUTBASE)"        catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_MANUAL)"/>' \
		'  <delegateURI uriStartString="$(VBOX_PATH_MANUAL_SRC)"                    catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_MANUAL)"/>' \
		'  <delegateURI uriStartString="$(VBOX_PATH_MANUAL_OUTBASE)"                catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_MANUAL)"/>' \
		'  <delegateURI uriStartString="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_MANUAL_SRC)"     catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_MANUAL)"/>' \
		'  <delegateURI uriStartString="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_MANUAL_OUTBASE)" catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_MANUAL)"/>' \
		'</catalog>'""",
            new_text=r"""		'<catalog xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">' \
		'  <delegatePublic publicIdStartString="-//OASIS/ENTITIES DocBook XML"      catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_DOCBOOK)"/>' \
		'  <delegatePublic publicIdStartString="-//OASIS/DTD DocBook XML"           catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_DOCBOOK)"/>' \
		'  <delegateSystem systemIdStartString="http://www.oasis-open.org/docbook/" catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_DOCBOOK)"/>' \
		'  <delegateSystem systemIdStartString="http://docbook.org/"                catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_DOCBOOK)"/>' \
		'  <delegateURI uriStartString="http://www.oasis-open.org/docbook/"         catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_DOCBOOK)"/>' \
		'  <delegateURI uriStartString="http://docbook.org/"                        catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_DOCBOOK)"/>' \
		'  <delegateSystem systemIdStartString="$(VBOX_PATH_MANUAL_SRC)"            catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_MANUAL)"/>' \
		'  <delegateSystem systemIdStartString="$(VBOX_PATH_MANUAL_SRC_SLASHED)"    catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_MANUAL)"/>' \
		'  <delegateSystem systemIdStartString="$(VBOX_PATH_MANUAL_OUTBASE)"        catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_MANUAL)"/>' \
		'  <delegateSystem systemIdStartString="$(VBOX_PATH_MANUAL_OUTBASE_SLASHED)" catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_MANUAL)"/>' \
		'  <delegateURI uriStartString="$(VBOX_PATH_MANUAL_SRC)"                    catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_MANUAL)"/>' \
		'  <delegateURI uriStartString="$(VBOX_PATH_MANUAL_SRC_SLASHED)"            catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_MANUAL)"/>' \
		'  <delegateURI uriStartString="$(VBOX_PATH_MANUAL_OUTBASE)"                catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_MANUAL)"/>' \
		'  <delegateURI uriStartString="$(VBOX_PATH_MANUAL_OUTBASE_SLASHED)"        catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_MANUAL)"/>' \
		'  <delegateURI uriStartString="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_MANUAL_SRC)"     catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_MANUAL)"/>' \
		'  <delegateURI uriStartString="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_MANUAL_OUTBASE)" catalog="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_XML_CATALOG_MANUAL)"/>' \
		'</catalog>'"""
        ),

        ReplacePair(
            old_text=r"""		'<catalog xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC)/common/oracle-accessibility-en.xml"            uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_MANUAL_SRC)/en_US/oracle-accessibility-en.xml"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC)/common/oracle-diversity.xml"					uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_MANUAL_SRC)/en_US/oracle-diversity.xml"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC)/common/oracle-support-en.xml"                  uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_MANUAL_SRC)/en_US/oracle-support-en.xml"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC)/en_US/user_ChangeLogImpl.xml"                  uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_MANUAL_SRC)/user_ChangeLogImpl.xml"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC)/titlepage-htmlhelp.xsl"                        uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_MANUAL_OUTBASE)/titlepage-htmlhelp.xsl"/>' \
		$(foreach x,user_VBoxManage_CommandsOverview.xml user_isomakercmd-man.xml $(addprefix user_,$(VBOX_MANUAL_XML_REFENTRY_FILES) man_VBoxHeadless.xml man_vboximg-mount.xml)\
		,'  <system systemId="$(VBOX_PATH_MANUAL_SRC)/en_US/$(x)"        uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_MANUAL_OUTBASE)/en_US/$(x)"/>') \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC)/en_US/SDKRef_apiref.xml"                       uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_MANUAL_OUTBASE)/en_US/SDKRef_apiref.xml"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC)/en_US/all-entities.ent"                        uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_MANUAL_OUTBASE)/all-entities.ent"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC)/html/docbook.xsl"                              uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_DOCBOOK)/html/docbook.xsl"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC)/html/chunk.xsl"                                uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_DOCBOOK)/html/chunk.xsl"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC)/htmlhelp/htmlhelp.xsl"                         uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_DOCBOOK)/htmlhelp/htmlhelp.xsl"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC)/manpages/docbook.xsl"                          uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_DOCBOOK)/manpages/docbook.xsl"/>' \
		'</catalog>'""",
            new_text=r"""		'<catalog xmlns="urn:oasis:names:tc:entity:xmlns:xml:catalog">' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC)/common/oracle-accessibility-en.xml"            uri="$(VBOX_PATH_MANUAL_SRC)/en_US/oracle-accessibility-en.xml"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC_SLASHED)/common/oracle-accessibility-en.xml"            uri="$(VBOX_PATH_MANUAL_SRC)/en_US/oracle-accessibility-en.xml"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC)/common/oracle-diversity.xml"					uri="$(VBOX_PATH_MANUAL_SRC)/en_US/oracle-diversity.xml"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC_SLASHED)/common/oracle-diversity.xml"					uri="$(VBOX_PATH_MANUAL_SRC)/en_US/oracle-diversity.xml"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC)/common/oracle-support-en.xml"                  uri="$(VBOX_PATH_MANUAL_SRC)/en_US/oracle-support-en.xml"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC_SLASHED)/common/oracle-support-en.xml"                  uri="$(VBOX_PATH_MANUAL_SRC)/en_US/oracle-support-en.xml"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC)/en_US/user_ChangeLogImpl.xml"                  uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_MANUAL_SRC)/user_ChangeLogImpl.xml"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC_SLASHED)/en_US/user_ChangeLogImpl.xml"                uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_MANUAL_SRC)/user_ChangeLogImpl.xml"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC)/titlepage-htmlhelp.xsl"                        uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_MANUAL_OUTBASE)/titlepage-htmlhelp.xsl"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC_SLASHED)/titlepage-htmlhelp.xsl"                      uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_MANUAL_OUTBASE)/titlepage-htmlhelp.xsl"/>' \
		$(foreach x,user_VBoxManage_CommandsOverview.xml user_isomakercmd-man.xml $(addprefix user_,$(VBOX_MANUAL_XML_REFENTRY_FILES) man_VBoxHeadless.xml man_vboximg-mount.xml)\
		,'  <system systemId="$(VBOX_PATH_MANUAL_SRC)/en_US/$(x)"         uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_MANUAL_OUTBASE)/en_US/$(x)"/>' \
		,'  <system systemId="$(VBOX_PATH_MANUAL_SRC_SLASHED)/en_US/$(x)" uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_MANUAL_OUTBASE)/en_US/$(x)"/>') \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC)/en_US/SDKRef_apiref.xml"                       uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_MANUAL_OUTBASE)/en_US/SDKRef_apiref.xml"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC_SLASHED)/en_US/SDKRef_apiref.xml"                     uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_MANUAL_OUTBASE)/en_US/SDKRef_apiref.xml"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC)/en_US/all-entities.ent"                        uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_MANUAL_OUTBASE)/all-entities.ent"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC_SLASHED)/en_US/all-entities.ent"                      uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_MANUAL_OUTBASE)/all-entities.ent"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC)/html/docbook.xsl"                              uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_DOCBOOK)/html/docbook.xsl"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC_SLASHED)/html/docbook.xsl"                            uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_DOCBOOK)/html/docbook.xsl"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC)/html/chunk.xsl"                                uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_DOCBOOK)/html/chunk.xsl"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC_SLASHED)/html/chunk.xsl"                              uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_DOCBOOK)/html/chunk.xsl"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC)/htmlhelp/htmlhelp.xsl"                         uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_DOCBOOK)/htmlhelp/htmlhelp.xsl"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC_SLASHED)/htmlhelp/htmlhelp.xsl"                       uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_DOCBOOK)/htmlhelp/htmlhelp.xsl"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC)/manpages/docbook.xsl"                          uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_DOCBOOK)/manpages/docbook.xsl"/>' \
		'  <system systemId="$(VBOX_PATH_MANUAL_SRC_SLASHED)/manpages/docbook.xsl"                          uri="file://$(VBOX_FILE_URL_MAYBE_SLASH)$(VBOX_PATH_DOCBOOK)/manpages/docbook.xsl"/>' \
		'</catalog>'"""
        )
    ],

    r"Config.kmk": [
        ReplacePair(
            old_text=r'''ifeq ($(KBUILD_HOST),darwin)
 VBOX_DARWIN_HOST_VERSION := $(subst ., ,$(shell uname -r))
 VBOX_DARWIN_HOST_VERSION_MAJOR := $(expr $(word 1, $(VBOX_DARWIN_HOST_VERSION)) - 4)
 VBOX_DARWIN_HOST_VERSION_MINOR := $(word 2, $(VBOX_DARWIN_HOST_VERSION))
 VBOX_DARWIN_HOST_VERSION_PATCH := $(word 3, $(VBOX_DARWIN_HOST_VERSION))
 VBOX_DARWIN_HOST_VERSION := 10.$(VBOX_DARWIN_HOST_VERSION_MAJOR).$(VBOX_DARWIN_HOST_VERSION_MINOR)
endif''',
            new_text=r'''ifeq ($(KBUILD_HOST),darwin)
 VBOX_DARWIN_HOST_VERSION := $(subst ., ,$(shell uname -r))
 VBOX_DARWIN_HOST_VERSION_MAJOR := $(expr $(word 1, $(VBOX_DARWIN_HOST_VERSION)) - 4)
 VBOX_DARWIN_HOST_VERSION_MINOR := $(word 2, $(VBOX_DARWIN_HOST_VERSION))
 VBOX_DARWIN_HOST_VERSION_PATCH := $(word 3, $(VBOX_DARWIN_HOST_VERSION))
 VBOX_DARWIN_HOST_VERSION := 10.$(VBOX_DARWIN_HOST_VERSION_MAJOR).$(VBOX_DARWIN_HOST_VERSION_MINOR)
endif

ifdef VBOX_INTEGRITY_CHECK
INTEGRITY_CHECK = /IntegrityCheck
else
INTEGRITY_CHECK = 
endif'''
        ),

        ReplacePair(
            old_text=r''' $$($(1)_0_OUTDIR)/$(n): $(2) $(VBOX_VERSION_STAMP) | $$(dir $$@)
	$(call MSG_TOOL,SIGNTOOL,,$<,$@)
	$(RM) -f -- "$@"
	$(CP) -- "$<" "$@"
	$(VBOX_VCC_EDITBIN) /LargeAddressAware /DynamicBase /NxCompat /Release /IntegrityCheck \
		/Version:$(VBOX_VERSION_MAJOR)0$(VBOX_VERSION_MINOR).$(VBOX_VERSION_BUILD) \
		"$@"
	$(call VBOX_SIGN_IMAGE_FN,$@)''',
            new_text=r''' $$($(1)_0_OUTDIR)/$(n): $(2) $(VBOX_VERSION_STAMP) | $$(dir $$@)
	$(call MSG_TOOL,SIGNTOOL,,$<,$@)
	$(RM) -f -- "$@"
	$(CP) -- "$<" "$@"
	$(VBOX_VCC_EDITBIN) /LargeAddressAware /DynamicBase /NxCompat /Release $(INTEGRITY_CHECK) \
		/Version:$(VBOX_VERSION_MAJOR)0$(VBOX_VERSION_MINOR).$(VBOX_VERSION_BUILD) \
		"$@"
	$(call VBOX_SIGN_IMAGE_FN,$@)'''
        )

    ]
}

REPLACE_CONTENT_TEST = {

    r"src\VBox\Runtime\r3\win\VBoxRT-openssl-1.1plus.def": [
        ReplacePair(
            old_text=r'''    ; tstRTBigNum.cpp
    BN_div
    BN_mul
    BN_mod_exp_simple
    BN_ucmp''',
            new_text=r'''    ; tstRTBigNum.cpp
    BN_div
    BN_mul
    BN_mod_exp_simple
    BN_ucmp

    ; VBoxRT.dll OpenSSL imports
    OpenSSL_version_num
    DH_generate_parameters_ex
    DH_new
    ASN1_STRING_get0_data'''
        )
    ]
}

REPLACE_CONTENT = {**REPLACE_CONTENT, **REPLACE_CONTENT_TABS}
