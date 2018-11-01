{
    "targets": [
        {
            "target_name": "addondemo",
            "sources": [
                "src/main.cc"
            ],
            "link_settings": {
                "conditions":[
                    ['OS=="mac"', {
                        "libraries": [
                            'Foundation.framework',
                            '-framework Test'
                        ],
                        "mac_framework_dirs": [
                            "../Framework",
                        ],
                        "include_dirs": [
                            "./Framework/Test.framework/Headers"
                        ],
                    }
                ]]
            },
            "xcode_settings": {
                "OTHER_CFLAGS": [
                    "-x objective-c++ -stdlib=libc++"
                ]
            },
        }
    ]
}