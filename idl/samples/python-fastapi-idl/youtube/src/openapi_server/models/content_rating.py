# coding: utf-8

from __future__ import annotations
from datetime import date, datetime  # noqa: F401

import re  # noqa: F401
from typing import Any, Dict, List, Optional  # noqa: F401

from pydantic import AnyUrl, BaseModel, EmailStr, validator  # noqa: F401


class ContentRating(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.

    ContentRating - a model defined in OpenAPI

        acb_rating: The acb_rating of this ContentRating [Optional].
        agcom_rating: The agcom_rating of this ContentRating [Optional].
        anatel_rating: The anatel_rating of this ContentRating [Optional].
        bbfc_rating: The bbfc_rating of this ContentRating [Optional].
        bfvc_rating: The bfvc_rating of this ContentRating [Optional].
        bmukk_rating: The bmukk_rating of this ContentRating [Optional].
        catv_rating: The catv_rating of this ContentRating [Optional].
        catvfr_rating: The catvfr_rating of this ContentRating [Optional].
        cbfc_rating: The cbfc_rating of this ContentRating [Optional].
        ccc_rating: The ccc_rating of this ContentRating [Optional].
        cce_rating: The cce_rating of this ContentRating [Optional].
        chfilm_rating: The chfilm_rating of this ContentRating [Optional].
        chvrs_rating: The chvrs_rating of this ContentRating [Optional].
        cicf_rating: The cicf_rating of this ContentRating [Optional].
        cna_rating: The cna_rating of this ContentRating [Optional].
        cnc_rating: The cnc_rating of this ContentRating [Optional].
        csa_rating: The csa_rating of this ContentRating [Optional].
        cscf_rating: The cscf_rating of this ContentRating [Optional].
        czfilm_rating: The czfilm_rating of this ContentRating [Optional].
        djctq_rating: The djctq_rating of this ContentRating [Optional].
        djctq_rating_reasons: The djctq_rating_reasons of this ContentRating [Optional].
        ecbmct_rating: The ecbmct_rating of this ContentRating [Optional].
        eefilm_rating: The eefilm_rating of this ContentRating [Optional].
        egfilm_rating: The egfilm_rating of this ContentRating [Optional].
        eirin_rating: The eirin_rating of this ContentRating [Optional].
        fcbm_rating: The fcbm_rating of this ContentRating [Optional].
        fco_rating: The fco_rating of this ContentRating [Optional].
        fmoc_rating: The fmoc_rating of this ContentRating [Optional].
        fpb_rating: The fpb_rating of this ContentRating [Optional].
        fpb_rating_reasons: The fpb_rating_reasons of this ContentRating [Optional].
        fsk_rating: The fsk_rating of this ContentRating [Optional].
        grfilm_rating: The grfilm_rating of this ContentRating [Optional].
        icaa_rating: The icaa_rating of this ContentRating [Optional].
        ifco_rating: The ifco_rating of this ContentRating [Optional].
        ilfilm_rating: The ilfilm_rating of this ContentRating [Optional].
        incaa_rating: The incaa_rating of this ContentRating [Optional].
        kfcb_rating: The kfcb_rating of this ContentRating [Optional].
        kijkwijzer_rating: The kijkwijzer_rating of this ContentRating [Optional].
        kmrb_rating: The kmrb_rating of this ContentRating [Optional].
        lsf_rating: The lsf_rating of this ContentRating [Optional].
        mccaa_rating: The mccaa_rating of this ContentRating [Optional].
        mccyp_rating: The mccyp_rating of this ContentRating [Optional].
        mcst_rating: The mcst_rating of this ContentRating [Optional].
        mda_rating: The mda_rating of this ContentRating [Optional].
        medietilsynet_rating: The medietilsynet_rating of this ContentRating [Optional].
        meku_rating: The meku_rating of this ContentRating [Optional].
        mena_mpaa_rating: The mena_mpaa_rating of this ContentRating [Optional].
        mibac_rating: The mibac_rating of this ContentRating [Optional].
        moc_rating: The moc_rating of this ContentRating [Optional].
        moctw_rating: The moctw_rating of this ContentRating [Optional].
        mpaa_rating: The mpaa_rating of this ContentRating [Optional].
        mpaat_rating: The mpaat_rating of this ContentRating [Optional].
        mtrcb_rating: The mtrcb_rating of this ContentRating [Optional].
        nbc_rating: The nbc_rating of this ContentRating [Optional].
        nbcpl_rating: The nbcpl_rating of this ContentRating [Optional].
        nfrc_rating: The nfrc_rating of this ContentRating [Optional].
        nfvcb_rating: The nfvcb_rating of this ContentRating [Optional].
        nkclv_rating: The nkclv_rating of this ContentRating [Optional].
        nmc_rating: The nmc_rating of this ContentRating [Optional].
        oflc_rating: The oflc_rating of this ContentRating [Optional].
        pefilm_rating: The pefilm_rating of this ContentRating [Optional].
        rcnof_rating: The rcnof_rating of this ContentRating [Optional].
        resorteviolencia_rating: The resorteviolencia_rating of this ContentRating [Optional].
        rtc_rating: The rtc_rating of this ContentRating [Optional].
        rte_rating: The rte_rating of this ContentRating [Optional].
        russia_rating: The russia_rating of this ContentRating [Optional].
        skfilm_rating: The skfilm_rating of this ContentRating [Optional].
        smais_rating: The smais_rating of this ContentRating [Optional].
        smsa_rating: The smsa_rating of this ContentRating [Optional].
        tvpg_rating: The tvpg_rating of this ContentRating [Optional].
        yt_rating: The yt_rating of this ContentRating [Optional].
    """

    acb_rating: Optional[str] = None
    agcom_rating: Optional[str] = None
    anatel_rating: Optional[str] = None
    bbfc_rating: Optional[str] = None
    bfvc_rating: Optional[str] = None
    bmukk_rating: Optional[str] = None
    catv_rating: Optional[str] = None
    catvfr_rating: Optional[str] = None
    cbfc_rating: Optional[str] = None
    ccc_rating: Optional[str] = None
    cce_rating: Optional[str] = None
    chfilm_rating: Optional[str] = None
    chvrs_rating: Optional[str] = None
    cicf_rating: Optional[str] = None
    cna_rating: Optional[str] = None
    cnc_rating: Optional[str] = None
    csa_rating: Optional[str] = None
    cscf_rating: Optional[str] = None
    czfilm_rating: Optional[str] = None
    djctq_rating: Optional[str] = None
    djctq_rating_reasons: Optional[List[str]] = None
    ecbmct_rating: Optional[str] = None
    eefilm_rating: Optional[str] = None
    egfilm_rating: Optional[str] = None
    eirin_rating: Optional[str] = None
    fcbm_rating: Optional[str] = None
    fco_rating: Optional[str] = None
    fmoc_rating: Optional[str] = None
    fpb_rating: Optional[str] = None
    fpb_rating_reasons: Optional[List[str]] = None
    fsk_rating: Optional[str] = None
    grfilm_rating: Optional[str] = None
    icaa_rating: Optional[str] = None
    ifco_rating: Optional[str] = None
    ilfilm_rating: Optional[str] = None
    incaa_rating: Optional[str] = None
    kfcb_rating: Optional[str] = None
    kijkwijzer_rating: Optional[str] = None
    kmrb_rating: Optional[str] = None
    lsf_rating: Optional[str] = None
    mccaa_rating: Optional[str] = None
    mccyp_rating: Optional[str] = None
    mcst_rating: Optional[str] = None
    mda_rating: Optional[str] = None
    medietilsynet_rating: Optional[str] = None
    meku_rating: Optional[str] = None
    mena_mpaa_rating: Optional[str] = None
    mibac_rating: Optional[str] = None
    moc_rating: Optional[str] = None
    moctw_rating: Optional[str] = None
    mpaa_rating: Optional[str] = None
    mpaat_rating: Optional[str] = None
    mtrcb_rating: Optional[str] = None
    nbc_rating: Optional[str] = None
    nbcpl_rating: Optional[str] = None
    nfrc_rating: Optional[str] = None
    nfvcb_rating: Optional[str] = None
    nkclv_rating: Optional[str] = None
    nmc_rating: Optional[str] = None
    oflc_rating: Optional[str] = None
    pefilm_rating: Optional[str] = None
    rcnof_rating: Optional[str] = None
    resorteviolencia_rating: Optional[str] = None
    rtc_rating: Optional[str] = None
    rte_rating: Optional[str] = None
    russia_rating: Optional[str] = None
    skfilm_rating: Optional[str] = None
    smais_rating: Optional[str] = None
    smsa_rating: Optional[str] = None
    tvpg_rating: Optional[str] = None
    yt_rating: Optional[str] = None

ContentRating.update_forward_refs()
