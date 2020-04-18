import numpy as np
import os
from .utils import Sequence

class TrackingNetDataset:
    """ TrackingNet test set.

    Publication:
        TrackingNet: A Large-Scale Dataset and Benchmark for Object Tracking in the Wild.
        Matthias Mueller,Adel Bibi, Silvio Giancola, Salman Al-Subaihi and Bernard Ghanem
        ECCV, 2018
        https://ivul.kaust.edu.sa/Documents/Publications/2018/TrackingNet%20A%20Large%20Scale%20Dataset%20and%20Benchmark%20for%20Object%20Tracking%20in%20the%20Wild.pdf

    Download the dataset using the toolkit https://github.com/SilvioGiancola/TrackingNet-devkit.
    """
    def __init__(self, dataset_path):
        self.base_path = dataset_path
        self.sequence_name_list = self._get_sequence_name_list()
        self.sequence_list = [self._construct_sequence(s) for s in self.sequence_name_list]

    def _construct_sequence(self, sequence_name):
        anno_path = '{}/{}/anno/{}.txt'.format(self.base_path, 'TEST', sequence_name)
        try:
            ground_truth_rect = np.loadtxt(str(anno_path), dtype=np.float64)
        except:
            ground_truth_rect = np.loadtxt(str(anno_path), delimiter=',', dtype=np.float64)

        frames_path = '{}/{}/frames/{}'.format(self.base_path, 'TEST', sequence_name)
        frame_list = [frame for frame in os.listdir(frames_path) if frame.endswith(".jpg")]
        frame_list.sort(key=lambda f: int(f[:-4]))
        frames_list = [os.path.join(frames_path, frame) for frame in frame_list]

        return Sequence(sequence_name, frames_list, ground_truth_rect.reshape(-1, 4))

    def _get_sequence_name_list(self):
        sequence_name_list = [  '-Dz7OIf54b0_0',
                                '-FCJqWfi9Wo_0',
                                '0-6LB4FqxoE_0',
                                '07Ysk1C0ZX0_0',
                                '0GER2Qd0vFw_0',
                                '0HBDWix1LAk_0',
                                '0HBDWix1LAk_1',
                                '0JOSlkhPOdA_0',
                                '0PRjEMNkNUs_0',
                                '0ZzhXi15dvo_0',
                                '0av1Erdno4A_0',
                                '0cP2LRl88qM_0',
                                '0cP2LRl88qM_1',
                                '0jgHdaQXpRk_0',
                                '0l7j7i3XhJ0_0',
                                '0mQjFeyN7LE_0',
                                '0nlxpC_f0wU_0',
                                '0ogRNrct_3c_0',
                                '11-hHR2lotQ_0',
                                '1AXqUQW2Vqs_0',
                                '1Jho-uH4dNY_0',
                                '1WIvjdxe4As_0',
                                '1Zgpv4GUFZk_0',
                                '1aAJHdfrJuk_0',
                                '1n0JQ2qIqLo_0',
                                '1n0JQ2qIqLo_1',
                                '1n0JQ2qIqLo_2',
                                '1qvKZsLFCX4_0',
                                '1qxEGelbWCg_0',
                                '1s7hqoYecSo_0',
                                '1tKzO_IhI34_0',
                                '1vn6Uo2NO7U_0',
                                '27HbwIQV92c_0',
                                '2DwR0E7MySc_0',
                                '2FVEzOxvjj8_0',
                                '2P0ok6kGdPk_0',
                                '2P0ok6kGdPk_1',
                                '2P0ok6kGdPk_2',
                                '2WTV7g1Z0lA_0',
                                '2e5XiuDEo5A_0',
                                '2h0_cHOXVD4_0',
                                '2r1mgtkZack_0',
                                '2rnnMNVuyYo_0',
                                '2uZQ7eqKpmY_0',
                                '2uZQ7eqKpmY_1',
                                '2uzSossy-P8_0',
                                '30y8Uy0B_uk_0',
                                '36_slnYU-EA_0',
                                '3CXY9-Y1ixc_0',
                                '3DE9R-UpL7w_0',
                                '3JmESCLz2Ic_0',
                                '3K_9VfzDHCA_0',
                                '3PVAsqby4jk_0',
                                '3jdzVaWohVw_0',
                                '3ynVtFJmIfk_0',
                                '43PlN1KVDgQ_0',
                                '49e2ryAo3Qw_0',
                                '4DkGRN8WXH0_0',
                                '4S48krFU3dQ_0',
                                '4T-m3KHtQPc_0',
                                '4XNrBaxkiHw_0',
                                '4YHgkyrL82M_0',
                                '4aMXjtIoC_M_0',
                                '4cCrF8kTOVE_0',
                                '4e0D1OyvPrI_0',
                                '4qXKgKaCd3s_0',
                                '4rT02vTH8qg_0',
                                '5-t2w-R1AHg_0',
                                '5AHb4xPDFR8_0',
                                '5P-KFY_sxEQ_0',
                                '5RJXgYSJaVE_0',
                                '5TqvkG4uWk0_0',
                                '5emtFao6IT4_0',
                                '5jyFpgIWzsE_0',
                                '60a_8DIqgJ0_0',
                                '67jcSw6ebUo_0',
                                '6Eci8o4MAVw_0',
                                '6OxBSJBe4tI_0',
                                '6XEKPSnk1QQ_0',
                                '6r3f3ICFPb8_0',
                                '6xzaKqU-rwI_0',
                                '79Y0wOFAwy0_0',
                                '79Y0wOFAwy0_1',
                                '7FZhTIGaL2c_0',
                                '7HnYRHuaCBk_0',
                                '7zFEmpHcIvo_0',
                                '88TIX-zand4_0',
                                '8Rsr0khg3Mk_0',
                                '8VkHx1GXvmo_0',
                                '8XhNvHbY4e0_0',
                                '8YBx-_bl8EA_0',
                                '8fiL0-tqkRA_0',
                                '8kkgVGMIf9Q_0',
                                '8r6QOyYh1vg_0',
                                '8sd513xQzV4_0',
                                '8wcZBX_BOwI_0',
                                '9F6LlyZ1GRI_0',
                                '9HizwmZHguc_0',
                                '9RKiTJdaVyY_0',
                                '9RmS4wETvRA_0',
                                '9XfvirWNWZA_0',
                                '9XozS-rat9w_0',
                                '9x6cMaE5cGA_0',
                                'A2AuBBONacU_0',
                                'A7OzWjZpCWs_0',
                                'AJhUA5hvAXQ_0',
                                'AVuFw6MIACg_0',
                                'Ajm-8msXIbc_0',
                                'B-bwz03_jTA_0',
                                'B7BM97SFv-E_0',
                                'BCJGL5E9huM_0',
                                'BE9f-YhCo50_0',
                                'BMVGTABB3O8_0',
                                'BN65-YWGSbs_0',
                                'BPX4cqYG6X0_0',
                                'BXJo9xrMxTo_0',
                                'B_-FCqaj4oc_0',
                                'BagyIW9DGsk_0',
                                'BhZMKM5wFs0_0',
                                'Bn4IVrCktF4_0',
                                'C08QnMjDfIc_0',
                                'C0YiKHm3jpw_0',
                                'C0YiKHm3jpw_1',
                                'CL55sbrvhrM_0',
                                'CPa9hv2pbd0_0',
                                'Cjc_wFsw4c4_0',
                                'ClmWyYJB5kE_0',
                                'Cp9cFTH-NMA_0',
                                'Cv-T-kmfraE_0',
                                'CyIhI7Vbzr0_0',
                                'D0jRA5TKT-o_0',
                                'DP9z5qDrrlY_0',
                                'DkquTEwWbaE_0',
                                'DoOmLuFnpi4_0',
                                'DstgtSNbx48_0',
                                'E3KU_oegSbg_0',
                                'E9RHw_-NN4c_0',
                                'EH4WB6TLXGs_0',
                                'EILr0LNw0Mg_0',
                                'EKp7rxqDbH8_0',
                                'E_cEXHKuMk4_0',
                                'EdQqy72QQeQ_0',
                                'EdQqy72QQeQ_1',
                                'EdQqy72QQeQ_2',
                                'EdQqy72QQeQ_3',
                                'EzTwnUAmGKc_0',
                                'FD0o9zxiCIQ_0',
                                'FMPxYweuarE_0',
                                'FSwyyml3QM8_0',
                                'FivbvMuiEWw_0',
                                'FpDI3f_tYj4_0',
                                'FuMNPiwPCWI_0',
                                'G22YjnFwQMs_0',
                                'G22YjnFwQMs_1',
                                'G22YjnFwQMs_2',
                                'G7JOHJ3za6Y_0',
                                'G9gkYQrgQGU_0',
                                'GG2nCfwA5cM_0',
                                'GaZr5KRTeIs_0',
                                'Gm0EO1-WVao_0',
                                'Gm0EO1-WVao_1',
                                'Gm0EO1-WVao_2',
                                'Gw5FxWOjKUE_0',
                                'H-RuyYTo-2o_0',
                                'HIZQ-O2OJlA_0',
                                'HZkjpcrz1zE_0',
                                'HaYoSNXNZ0M_0',
                                'Het2PkZCfGs_0',
                                'HoWrvbRF5Uw_0',
                                'Hu3nL3Famhk_0',
                                'I-rzzVQXf9w_0',
                                'IQrzZwkXQlI_0',
                                'ITHvD6BDzXc_0',
                                'IUhkjSSb9a8_0',
                                'Ij38IL41xQQ_0',
                                'Iwq0hcVjm7w_0',
                                'IxjBypJ83pA_0',
                                'IxjDSJuPY24_0',
                                'IyBEsH1acKM_0',
                                'J6AFXbjd1uo_0',
                                'J6OlMtgrAC8_0',
                                'J6tnw6IzT44_0',
                                'J73waS0d02Y_0',
                                'JOfVj6FgUF0_0',
                                'JkLxB0XYOGM_0',
                                'Jrp6_6bUBkk_0',
                                'Jv72bvabmCc_0',
                                'JyT9qPb5Fe0_0',
                                'KCOkbH1kfDU_0',
                                'KCOkbH1kfDU_1',
                                'KH2kdBdUUyA_0',
                                'KMqR27j3Mhg_0',
                                'KRrT2XwHHWU_0',
                                'KYio1UJatAk_0',
                                'KZgwt7A73J0_0',
                                'KbaTy9bm_Mo_0',
                                'KbaTy9bm_Mo_1',
                                'KcOBOusRanQ_0',
                                'L2vzunH67iA_0',
                                'LLTG_b2bALQ_0',
                                'LLhYjizenC4_0',
                                'LP1JQ6r-LR8_0',
                                'LcKCWQgxPv4_0',
                                'MJZ2kt2kqSU_0',
                                'MiZ66gM5tzw_0',
                                'MlxbHhZ7jVw_0',
                                'Mw8KpkA0SRc_0',
                                'Mw8KpkA0SRc_1',
                                'N0Wa8DgCTL4_0',
                                'N5MiDo3aX1A_0',
                                'N5VpKWs1wm4_0',
                                'NPpbrvMWJXA_0',
                                'NV4_J7uoFYw_0',
                                'Nn4-s0CETPg_0',
                                'O-bhixil5Ho_0',
                                'O1QjMCPJn5A_0',
                                'O3ZT6MVSHZ4_0',
                                'O4UttlHCp28_0',
                                'O6AtzcBBo2A_0',
                                'O7YXEoG1ZwM_0',
                                'OGkySddv1S0_0',
                                'OJHDGvFgFFw_0',
                                'OMCNuZOFEi0_0',
                                'OQMG0C015rI_0',
                                'OU72LG0O9_M_0',
                                'OpuH-1YGcY8_0',
                                'OxQbu0kwObo_0',
                                'PFMJouhE468_0',
                                'PYY3bfUgooc_0',
                                'PYY3bfUgooc_1',
                                'PYY3bfUgooc_2',
                                'PYrNrXR5UUw_0',
                                'PZ1bSGqtAdw_0',
                                'Q427Xs_icsw_0',
                                'QDxAH3cfiDI_0',
                                'QJ6PebrVhb4_0',
                                'QS2qDrnVQFo_0',
                                'QYb6ChPTcHY_0',
                                'QcH9cV-kaho_0',
                                'R-5JSKO4sVc_0',
                                'R6z-5RKwFfA_0',
                                'RAUpWkFRwdA_0',
                                'RAUpWkFRwdA_1',
                                'RHV8r6lwmFI_0',
                                'RIyWvrmneHQ_0',
                                'R_2Kscz8YBE_0',
                                'R_2Kscz8YBE_1',
                                'RkpCxP_8kDM_0',
                                'SHygnt65pM0_0',
                                'SSfdIHgb4IU_0',
                                'SZjSU00vWPQ_0',
                                'SkztYkUK6K8_0',
                                'SmZl-r92pmk_0',
                                'T-6SBApMCsw_0',
                                'T1U6bPMinzw_0',
                                'T7Jr0u4xxM0_0',
                                'TPf68wTe3IU_0',
                                'TdkeFfjNUpg_0',
                                'ThudiuJW5Kg_0',
                                'TyR2X9M_NOI_0',
                                'UUyk7Eojl1I_0',
                                'UecVWTt2ChA_0',
                                'UlYxD4JVRhI_0',
                                'V7ZB7vVnukg_0',
                                'VT_Bw6ANlY0_0',
                                'Vgn-TZkzDV0_0',
                                'VoETGQZ3HKA_0',
                                'VpXVVpIesQo_0',
                                'WJMReV7XiNM_0',
                                'Wh0YJ3JBIzU_0',
                                'Wo1TKyYU4ow_0',
                                'WsaOn85TqUE_0',
                                'WtFNGOMs_zY_0',
                                'XKdyEYXltZo_0',
                                'XX1eVms9ZcE_0',
                                'XX1eVms9ZcE_1',
                                'XX1eVms9ZcE_2',
                                'Xg6lP1zsq_E_0',
                                'Xj5Tt01VsIk_0',
                                'XwyyGjLi7pc_0',
                                'Xzu094YlBHQ_0',
                                'YaXKZdSEwt4_0',
                                'YfjTQdBZwCU_0',
                                'YhrkfDzeLdI_0',
                                'YtN78tgbMfE_0',
                                'Z968B3Un4sA_0',
                                'ZA2emnqIhLE_0',
                                'ZGFj8HFpeEQ_0',
                                'ZIihz5uxPiE_0',
                                'ZIkbtAE_F3I_0',
                                'Zljto-7mKTI_0',
                                '_-er1Sdg3a8_0',
                                '_-yTvT_dGw8_0',
                                '_3GIPsDKoVk_0',
                                '_JAp8QynvQE_0',
                                '_O85LwqCB7k_0',
                                '_RBD5erECJ8_0',
                                '_X5QH6Bxm8o_0',
                                '__WaG8fRMto_0',
                                '_dKKBSKYStE_0',
                                '_tcyjMmMSRk_0',
                                'a-WtA7RZRwc_0',
                                'a4kJCIe8e2c_0',
                                'a5wWW5xspOg_0',
                                'aAsiYXsj28E_0',
                                'aBLH8qvaIFg_0',
                                'aKg7xivrI9Y_0',
                                'agdU9QeRP9g_0',
                                'akbBUSKnyj8_0',
                                'an_Xwal5AsM_0',
                                'an_Xwal5AsM_1',
                                'apGi_6BR3nc_0',
                                'as3_Rkdv0SU_0',
                                'ay65MRWqiRk_0',
                                'ayvfySqnxWA_0',
                                'b-PQEq-ehas_0',
                                'b0mx69LQbp0_0',
                                'b64ORExZ1B8_0',
                                'bHE3l9EpRsA_0',
                                'bR82aIlMUFw_0',
                                'bYmvxWFTkJQ_0',
                                'ba5w79A8b1U_0',
                                'begVPWOxPRs_0',
                                'bl-jwa1jRTE_0',
                                'btDFQ9fJZX4_0',
                                'buRfiT3Mq6Q_0',
                                'cCRlul2kpr0_0',
                                'cCRlul2kpr0_1',
                                'cJ91NTO2KTQ_0',
                                'cNqf75UKk9M_0',
                                'cNqf75UKk9M_1',
                                'cOIk7Ypfoxk_0',
                                'cxsFItvKQNQ_0',
                                'd0PqI5peh4Y_0',
                                'd102whT2D6s_0',
                                'dFk2XOr1cuw_0',
                                'dFk2XOr1cuw_1',
                                'dPLbMJnofdE_0',
                                'dvzgPFeUtQE_0',
                                'e0YuX0Nri9M_0',
                                'e51Nyo7236o_0',
                                'eCfpscj3SMk_0',
                                'eIzIge4GW-U_0',
                                'eZX7H5XfoE4_0',
                                'ee2xCtzwt7A_0',
                                'eku6SgAEK4A_0',
                                'eo8SMTqCWwY_0',
                                'eqbbWCUnq-g_0',
                                'f11fVFiaNIw_0',
                                'fAzgoRh2yP0_0',
                                'fHYqnq-VjK8_0',
                                'fJN4flFKqU8_0',
                                'fMR7bO9fQMc_0',
                                'fRaQFA8HOvg_0',
                                'fTDFgcZAPUU_0',
                                'fZ-sAPmffuw_0',
                                'fZ-sAPmffuw_1',
                                'fbPpRBquwU0_0',
                                'fk1SMEpHgyM_0',
                                'fq_rMea3B9s_0',
                                'fq_rMea3B9s_1',
                                'gP7HK4zH1vI_0',
                                'gcoZEf8SRvs_0',
                                'gcoZEf8SRvs_1',
                                'gcoZEf8SRvs_2',
                                'gfVJeD4IIlw_0',
                                'giGciyARCG4_0',
                                'gvErAQRk-nQ_0',
                                'gwIgX3xL4zk_0',
                                'gzy37sBMZlk_0',
                                'h8gWHQQBD9g_0',
                                'hSmgyZ0oy6U_0',
                                'hSmgyZ0oy6U_1',
                                'hTJPyyjLi24_0',
                                'hXTRhpolmkQ_0',
                                'h_64CL5t2y4_0',
                                'hdk-XX3S_tM_0',
                                'hnNJRmj7NFI_0',
                                'hwr9MZnrBRw_0',
                                'i21zdDckboY_0',
                                'i6QcVTVjAjs_0',
                                'iCmWVMcSnh4_0',
                                'iCmWVMcSnh4_1',
                                'iU0dAzhq1GI_0',
                                'ii_w8og8RXg_0',
                                'izh4_B0XmNA_0',
                                'j2-2mjNcxJA_0',
                                'jEtyhipY4d0_0',
                                'jFkgSp701zg_0',
                                'jR59o-HIJjE_0',
                                'jV3zR962zg4_0',
                                'k-0upTJLhDw_0',
                                'k7fWxZG_nr0_0',
                                'k8NKq047jDk_0',
                                'kFk1Okfsv00_0',
                                'kLE7wS8RjhI_0',
                                'kODMnbgJnhY_0',
                                'kPovigNRbNo_0',
                                'kPovigNRbNo_1',
                                'kYdlI6WkjIc_0',
                                'kfSisxelhIA_0',
                                'kjakNVBtscI_0',
                                'kjq9Uhrwgy8_0',
                                'kmWAD0fCAUc_0',
                                'kqVQL2DTzrA_0',
                                'kwbNF-PwnO0_0',
                                'l0H68D1NqyQ_0',
                                'lU8bT96R7nw_0',
                                'l_nUdlgO3-8_0',
                                'laxtGQ7qayc_0',
                                'lnefnJLRsv8_0',
                                'm6lV1lfv7GE_0',
                                'mJuTbvcmd6k_0',
                                'mQdYPE128d0_0',
                                'n5Kc6zOUqTA_0',
                                'nHpL3SlCABM_0',
                                'nQAvmpBuJn0_0',
                                'nSF4Wwfgv00_0',
                                'ncw0BVKIdHI_0',
                                'nyFqvPD4OyE_0',
                                'o1T0yeEntU0_0',
                                'o7bcGRR1UEE_0',
                                'o7bcGRR1UEE_1',
                                'oFFmJZeBgQM_0',
                                'oSvNLf17JmQ_0',
                                'od3E3QIzwe0_0',
                                'oinBYXKdc14_0',
                                'oqHsiHMcWs4_0',
                                'ovOPcZq3U6s_0',
                                'ovOPcZq3U6s_1',
                                'pFqkmzbiF78_0',
                                'pNhXwX7UW1Q_0',
                                'pOHPrcoNraU_0',
                                'poIBw8DkHxI_0',
                                'qacehFLfCxE_0',
                                'qeWQ_UccmwA_0',
                                'r179UQZYkKM_0',
                                'r9CYddJQDDg_0',
                                'rHipntra6do_0',
                                'rIKZtfg3d4k_0',
                                'rIKZtfg3d4k_1',
                                'rIKZtfg3d4k_2',
                                'rNH3Pzt8Qlg_0',
                                'rac0fmoIBtI_0',
                                'rac0fmoIBtI_1',
                                'rdVo1ikBoJA_0',
                                'rh_yH1TWvds_0',
                                'rmuT5bGj3k8_0',
                                'rw00mXyICtw_0',
                                'rwOUiIA73mY_0',
                                'rwOUiIA73mY_1',
                                's64u9YcHWck_0',
                                'sYvXze9K6r4_0',
                                't0b4xbXP0qI_0',
                                'tBa7zZXyr-w_0',
                                'tMC9xJlxU9g_0',
                                'tRCSL0Gf_5U_0',
                                'tUC-gVlXPhE_0',
                                'te-LKtIbi9Q_0',
                                'ti0klt7W7GM_0',
                                'tlxGSBruCR8_0',
                                'tlxGSBruCR8_1',
                                'tp2E-Ep_pDg_0',
                                'tv2_ONbSPis_0',
                                'twF79jlTCZU_0',
                                'tyJRdktEY-c_0',
                                'uN-CPT1r4gQ_0',
                                'uVP5RZybJpI_0',
                                'uVjOanE0huc_0',
                                'uVjOanE0huc_1',
                                'ucj68YW8xKQ_0',
                                'ueOjJwCqQ9U_0',
                                'us3OFIQ4os0_0',
                                'vAksZpr6FuA_0',
                                'vDgIdwY9RGA_0',
                                'vQ9dIV-HJT0_0',
                                'vbCFd2ppCgk_0',
                                'vh-k83DtNTQ_0',
                                'vrA63WFr7gk_0',
                                'vxIr9qvzroQ_0',
                                'w-6wN_vsCbA_0',
                                'w-eM3-d3tLM_0',
                                'w04NTNZSpj8_0',
                                'w1RAnmIgBaU_0',
                                'wIXF1OmxzrA_0',
                                'wLOH3ZACIz8_0',
                                'wN4jdoroP9o_0',
                                'wRDRtaxcsQg_0',
                                'wUrEV3FNsJk_0',
                                'wlTb-A_C-2Y_0',
                                'xA2ZIXWuqxY_0',
                                'xFkcP0iqrhQ_0',
                                'xI0y9eav0ME_0',
                                'xRM3n5N0cYc_0',
                                'xUUQmAPnDGI_0',
                                'xhMLKMgaN9w_0',
                                'xmA3NTeiNB4_0',
                                'xyjpLpgrxtA_0',
                                'y-DH0Xn9Bg0_0',
                                'y0soO7I-tjk_0',
                                'yGUg7Qqho9c_0',
                                'yPsZexppduA_0',
                                'yiXgmk43Odw_0',
                                'yiZ3grdDYIo_0',
                                'yz_Hg4vcFPA_0',
                                'z25IhPQry_M_0',
                                'z2BgjH_CtIA_0',
                                'zCLWwZOFSDY_0',
                                'za7pL4OB-_o_0',
                                'zqt_c00WM-Q_0',
                                'zxTw_b64trk_0']

        return sequence_name_list
