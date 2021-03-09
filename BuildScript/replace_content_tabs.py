from replace_pair import ReplacePair


REPLACE_CONTENT_TABS = {

    r"src\VBox\Runtime\Makefile.kmk": [
        ReplacePair(
            old_text=r'''VBoxRT_LIBS.win                = \
	$(PATH_SDK_$(VBOX_WINDDK)_LIB)/vccomsup.lib \
	$(PATH_SDK_$(VBOX_WINDDK)_LIB)/wbemuuid.lib \
	$(PATH_TOOL_$(VBOX_VCC_TOOL)_LIB)/delayimp.lib''',
            new_text=r'''VBoxRT_LIBS.win                = \
	$(PATH_SDK_$(VBOX_WINDDK)_LIB)/vccomsup.lib \
	$(PATH_SDK_$(VBOX_WINDDK)_LIB)/wbemuuid.lib \
	$(PATH_TOOL_$(VBOX_VCC_TOOL)_LIB)/delayimp.lib \
	$(PATH_SDK_$(VBOX_WINPSDK)_LIB)/crypt32.lib \
	$(PATH_SDK_$(VBOX_WINPSDK)_LIB)/bcrypt.lib'''
        ),

        ReplacePair(
            old_text=r'''VBoxRT-x86_LIBS.win                = \
	$(PATH_SDK_$(VBOX_WINDDK)_LIB.x86)/vccomsup.lib \
	$(PATH_SDK_$(VBOX_WINDDK)_LIB.x86)/wbemuuid.lib \
	$(PATH_TOOL_$(VBOX_VCC_TOOL_STEM)X86_LIB)/delayimp.lib''',
            new_text=r'''VBoxRT-x86_LIBS.win                = \
	$(PATH_SDK_$(VBOX_WINDDK)_LIB.x86)/vccomsup.lib \
	$(PATH_SDK_$(VBOX_WINDDK)_LIB.x86)/wbemuuid.lib \
	$(PATH_TOOL_$(VBOX_VCC_TOOL_STEM)X86_LIB)/delayimp.lib \
	$(PATH_SDK_$(VBOX_WINPSDK)_LIB.x86)/crypt32.lib \
	$(PATH_SDK_$(VBOX_WINPSDK)_LIB.x86)/bcrypt.lib'''
        )
    ]
}
