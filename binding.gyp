{
    "targets": [
        {
            "target_name": "NativeExtension",
            "sources": [ "NativeExtension/NativeExtension.cc", "NativeExtension/functions.cc" ],
            "include_dirs" : [
 	 			"<!(node -e \"require('nan')\")"
			]
        }
    ],
}
