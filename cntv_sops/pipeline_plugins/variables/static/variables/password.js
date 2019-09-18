(function () {
    $.atoms.password = [
        {
            tag_code: "password",
            type: "password",
            attrs: {
                name: gettext("密码"),
                hookable: true,
                validation: [
                    {
                        type: "required"
                    }
                ]
            }
        },
    ]
})();
