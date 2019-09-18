(function () {
    $.atoms.cc_replace_fault_machine = [
        {
            tag_code: "cc_host_replace_detail",
            type: "datatable",
            attrs: {
                name: gettext("主机详情"),
                empty_text: gettext("请至少添加一条数据"),
                editable: true,
                add_btn: true,
                columns: [
                    {
                        tag_code: "cc_fault_ip",
                        type: "input",
                        attrs: {
                            name: gettext("故障机IP"),
                            editable: true,
                            validation: [
                                {
                                    type: "required"
                                }
                            ]
                        }
                    },
                    {
                        tag_code: "cc_new_ip",
                        type: "input",
                        attrs: {
                            name: gettext("替换机IP"),
                            editable: true,
                            validation: [
                                {
                                    type: "required"
                                }
                            ]
                        }
                    }
                ],
                hookable: true,
                validation: [
                    {
                        type: "required"
                    }
                ]
            }
        }
    ]
})();