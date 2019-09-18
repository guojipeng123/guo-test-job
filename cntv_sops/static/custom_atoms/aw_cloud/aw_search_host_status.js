
(function () {
    $.atoms.aw_search_host_status = [
        {
            tag_code: "host_id_list",
            type: "input",
            attrs: {
                name: gettext("主机ID"),
                placeholder: gettext("主机ID"),
                hookable: true
            },
            validation: [
                {
                    type: "required"
                }
            ]
        },
        {
            tag_code: "domain_id",
            type: "input",
            attrs: {
                name: gettext("部门ID"),
                placeholder: gettext("部门ID"),
                hookable: true
            },
            validation: [
                {
                    type: "required"
                }
            ]
        },
        {
            tag_code: "project_id",
            type: "input",
            attrs: {
                name: gettext("项目ID"),
                placeholder: gettext("项目ID"),
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

