
(function () {
    $.atoms.bk_api_test = [
        {
            tag_code: "api",
            type: "input",
            attrs: {
                name: gettext("api"),
                placeholder: gettext("api"),
                hookable: true
            },
            validation: [
                {
                    type: "required"
                }
            ]
        },
        {
            tag_code: "bk_username",
            type: "input",
            attrs: {
                name: gettext("bk_username"),
                placeholder: gettext("用户名"),
                hookable: true
            },
            validation: [
                {
                    type: "required"
                }
            ]
        },
        {
            tag_code: "extra_dict",
            type: "input",
            attrs: {
                name: gettext("额外参数"),
                placeholder: gettext("请输入"),
                hookable: true
            },
            validation: [
            ]
        }
    ]
})();

