
(function () {
    $.atoms.find_job_test = [
        {
            tag_code: "bk_username",
            type: "input",
            attrs: {
                name: gettext("当前用户"),
                placeholder: gettext("请输入当前用户名称"),
                hookable: true
            },
            validation: [
                {
                    type: "required"
                }
            ]
},
        {
            tag_code: "bk_biz_id",
            type: "input",
            attrs: {
                name: gettext("业务ID"),
                placeholder: gettext("请输入需要查询的业务ID"),
                hookable: true
            },
            validation: [
                {
                    type: "required"
                }
            ]
        },
        {
            tag_code: "job_instance_id",
            type: "input",
            attrs: {
                name: gettext("任务ID"),
                placeholder: gettext("请输入需要查询的任务ID"),
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
