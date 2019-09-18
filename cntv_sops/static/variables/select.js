(function () {
    $.atoms.select = [
        {
            tag_code: "select",
            meta_transform: function (variable) {
                let metaConfig = variable.value;
                let remote = false;
                let remote_url = "";
                let items = [];
                let placeholder = '';
                if (metaConfig.datasource === "1") {
                    remote_url = metaConfig.items_text;
                    remote = true;
                } else {
                    try {
                        items = JSON.parse(metaConfig.items_text);
                    } catch (err) {
                        items = [];
                        placeholder = gettext('非法下拉框数据源，请检查您的配置');
                    }
                    if (!(items instanceof Array)) {
                        items = [];
                        placeholder = gettext('非法下拉框数据源，请检查您的配置');
                    }
                }

                let multiple = false;
                let default_val = metaConfig.default || '';

                if (metaConfig.type === "1") {
                    multiple = true;
                    default_val = [];
                    if (metaConfig.default) {
                        let vals = metaConfig.default.split(',');
                        for (let i in vals) {
                            default_val.push(vals[i].trim());
                        }
                    }
                }
                return {
                    tag_code: this.tag_code,
                    type: "select",
                    attrs: {
                        name: gettext("下拉框"),
                        hookable: false,
                        items: items,
                        multiple: multiple,
                        value: default_val,
                        remote: remote,
                        remote_url: remote_url,
                        placeholder: placeholder,
                        remote_data_init: function (data) {
                            return data
                        },
                        validation: [
                            {
                                type: "required"
                            }
                        ]
                    }
                }
            }
        }
    ]
})();
