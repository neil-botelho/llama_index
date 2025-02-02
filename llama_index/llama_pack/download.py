from typing import Type

from llama_index.download.download_utils import LLAMA_HUB_URL, download_llama_module
from llama_index.llama_pack.base import BaseLlamaPack


def download_llama_pack(
    llama_pack_class: str,
    download_dir: str,
    llama_hub_url: str = LLAMA_HUB_URL,
    refresh_cache: bool = False,
) -> Type[BaseLlamaPack]:
    """Download a single LlamaPack from Llama Hub.

    Args:
        llama_pack_class: The name of the LlamaPack class you want to download,
            such as `GmailOpenAIAgentPack`.
        refresh_cache: If true, the local cache will be skipped and the
            loader will be fetched directly from the remote repo.
        download_dir: Custom dirpath to download the pack into.

    Returns:
        A Loader.
    """
    pack_cls = download_llama_module(
        llama_pack_class,
        llama_hub_url=llama_hub_url,
        refresh_cache=refresh_cache,
        custom_path=download_dir,
        library_path="llama_packs/library.json",
        disable_library_cache=True,
    )
    if not issubclass(pack_cls, BaseLlamaPack):
        raise ValueError(f"Tool class {pack_cls} must be a subclass of BaseToolSpec.")

    return pack_cls
