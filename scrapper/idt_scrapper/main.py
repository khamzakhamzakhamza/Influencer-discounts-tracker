import inject
from inject import Binder
from idt_scrapper.domain.di_injections import domain_di_config
from idt_scrapper.domain.orchestrators.update_orchestrator import UpdateOrchestrator
from idt_scrapper.domain.services.influencer_service import InfluencerService
from idt_scrapper.domain.services.content_service import ContentService
from idt_scrapper.infrastructure.di_injections import infrastructure_di_config

def startup() -> UpdateOrchestrator:
    inject.configure(di)

    return UpdateOrchestrator(inject.instance(InfluencerService), inject.instance(ContentService))

def di(binder: Binder):
    infrastructure_di_config(binder)
    domain_di_config(binder)