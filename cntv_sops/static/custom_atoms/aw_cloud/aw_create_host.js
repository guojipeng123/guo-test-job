
(function () {
    $.atoms.aw_create_host = [
        {
            tag_code: "work_data",
            type: "input",
            attrs: {
                name: gettext("创建主机Json"),
                placeholder: gettext("创建主机所需要的参数"),
                hookable: true
            },
            validation: [
                {
                    type: "required"
                }
            ]
        },
    ]
})();

