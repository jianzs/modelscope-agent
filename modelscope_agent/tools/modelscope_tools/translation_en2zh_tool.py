from .pipeline_tool import ModelscopePipelineTool


class TranslationEn2ZhTool(ModelscopePipelineTool):
    default_model = 'damo/nlp_csanmt_translation_en2zh'
    description = '根据输入指令，将相应的英文文本翻译成中文回复'
    name = 'text-translation-en2zh'
    parameters: list = [{
        'name': 'input',
        'description': '用户输入的英文文本',
        'required': True,
        'type': 'string'
    }]

    def call(self, params: str, **kwargs) -> str:
        result = super().call(params, **kwargs)
        zh = result['Data']['translation']
        return zh

    # def _parse_output(self, origin_result, *args, **kwargs):
    #     return {'result': origin_result['translation']}
