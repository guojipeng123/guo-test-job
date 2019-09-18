(function () {
    $.atoms.select_meta = [
        {
            tag_code: "select",
            type: "combine",
            attrs: {
                name: gettext("下拉框"),
                hookable: true,
                children: [
                    {
                        tag_code: "datasource",
                        type: "radio",
                        attrs: {
                            name: gettext("数据源"),
                            hookable: true,
                            items: [{name: gettext("自定义"), value: "0"}, {name: gettext("远程数据源"), value: "1"}],
                            value: "0",
                            validation: [
                                {
                                    type: "required"
                                }
                            ]
                        }
                    },
                    {
                        tag_code: "items_text",
                        type: "textarea",
                        attrs: {
                            name: gettext("选项"),
                            hookable: true,
                            placeholder: gettext('请输入数据源信息，自定义数据源格式为 [{"text": "", "value": ""}...}]，若是远程数据源则填写返回该格式数据的 URL'),
                            validation: [
                                {
                                    type: "required"
                                }
                            ]
                        }
                    },
                    {
                        tag_code: "type",
                        type: "radio",
                        attrs: {
                            name: gettext("类型"),
                            hookable: true,
                            items: [{name: gettext("单选"), value: "0"}, {name: gettext("多选"), value: "1"}],
                            value: "0",
                            validation: [
                                {
                                    type: "required"
                                }
                            ]
                        }
                    },
                    {
                        tag_code: "default",
                        type: "textarea",
                        attrs: {
                            name: gettext("默认值"),
                            placeholder: gettext("请输入下拉框的默认值，单选为 value 的格式，多选为 value,value,... 的格式"),
                            hookable: true,
                        }
                    }
                ]
            }

        },
    ]
})();
