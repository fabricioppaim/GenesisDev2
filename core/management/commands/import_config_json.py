import json
from django.core.management.base import BaseCommand
from empresas.models import Empresa
from ambientes.models import Ambiente
from bancodedados.models import BancoDeDados, BancoDados
from webs.models import Web
from projetos.models import Projeto
from gams.models import GAM
from loggenexus.models import LogGenexus
from genexus.models import Genexus
from credenciais.models import Credencial

class Command(BaseCommand):
    help = 'Importa dados de configurações a partir de um arquivo JSON.'

    def add_arguments(self, parser):
        parser.add_argument('json_path', type=str, help='Caminho do arquivo JSON de configurações')

    def handle(self, *args, **options):
        with open(options['json_path'], encoding='utf-8') as f:
            data = json.load(f)

        # Empresas
        for empresa in data.get('Empresa', []):
            Empresa.objects.get_or_create(
                name=empresa['Name'],
                domain=empresa['Domain'],
                ativo=empresa['Ativo']
            )

        # Ambientes
        ambiente_map = {}
        for ambiente in data.get('Ambiente', []):
            obj, _ = Ambiente.objects.get_or_create(
                name=ambiente['Name'],
                sufixo=ambiente['Sufixo'],
                ativo=ambiente['Ativo']
            )
            ambiente_map[ambiente['Id']] = obj

        # Bancos de Dados
        for bd in data.get('BancoDeDados', []):
            bd_obj, _ = BancoDeDados.objects.get_or_create(
                name=bd['Name'],
                service_name=bd['ServiceName'],
                engine=bd['Engine']
            )
            for amb_id in bd.get('AmbienteId', []):
                bd_obj.ambientes.add(ambiente_map.get(amb_id))
            for banco in bd.get('BancoDados', []):
                BancoDados.objects.get_or_create(
                    banco_de_dados=bd_obj,
                    name=banco['Name'],
                    user_id_jenkis=banco['UserIdJenkis']
                )

        # Webs
        for web in data.get('Web', []):
            web_obj, _ = Web.objects.get_or_create(
                name=web['Name'],
                path=web['Path'],
                shared=web['Shared'],
                finalidade=web['Finalidade']
            )
            for amb_id in web.get('AmbienteId', []):
                web_obj.ambientes.add(ambiente_map.get(amb_id))

        # Projetos
        for projeto in data.get('Projetos', []):
            Projeto.objects.get_or_create(
                name=projeto['Name'],
                version=projeto.get('version', ''),
                server_kb_alias=projeto.get('ServerKBAlias', ''),
                kb_version=projeto.get('KbVersion', ''),
                target_path=projeto.get('TargetPath', ''),
                arquivos_complementares=projeto.get('ArquivosComplementares', ''),
                exclude_files=projeto.get('ExcludeFiles', ''),
                directory_config_msbuild=projeto.get('DirectoryConfigMsBuild', ''),
                base_gam=projeto.get('BaseGAM', False),
                https=projeto.get('Https', False)
            )

        # GAM
        for gam in data.get('GAM', []):
            gam_obj, _ = GAM.objects.get_or_create(
                user_id_gam_admin=gam['UserIDGamAdmin'],
                user_id_gam_connection=gam['UserIDGamConnection']
            )
            for amb_id in gam.get('AmbienteId', []):
                gam_obj.ambientes.add(ambiente_map.get(amb_id))

        # LogGenexus
        for log in data.get('LogGenexus', []):
            log_obj, _ = LogGenexus.objects.get_or_create(
                conversion_pattern=log['ConversionPattern']
            )
            for amb_id in log.get('AmbienteId', []):
                log_obj.ambientes.add(ambiente_map.get(amb_id))

        # Genexus
        for gx in data.get('Genexus', []):
            Genexus.objects.get_or_create(
                gx_server_url=gx.get('GxServerUrl', ''),
                gx_server_version=gx.get('GxServerVersion', ''),
                gx_server_working_directory=gx.get('GXServerWorkingDirectory', ''),
                gx_server_working_directory_kb=gx.get('GXServerWorkingDirectoryKB', '')
            )

        # Credenciais
        for cred in data.get('Credenciais', []):
            Credencial.objects.get_or_create(
                name=cred['Name'],
                cred_id=cred['Id']
            )

        self.stdout.write(self.style.SUCCESS('Importação concluída com sucesso!'))
