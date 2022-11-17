@router.post("/antecipe/request-code", status_code=201)
def route_request_code(
        data: CodeIn,
        sms: SMSService = Depends(SMSService),
        db: Session = Depends(get_db)
):
    # todo: verificar se sms já foi enviado

    code = SmsCode()
    code.transaction_id = data.transaction_id
    code.code = str(randint(1000, 9999))
    code.status = False

    query = select(CprFormModel).where(CprFormModel.transaction_id == data.transaction_id)
    cpr_data: CprFormModel | None = db.execute(query).scalar()
    if cpr_data is None:
        raise ResponseException.not_found("Dados do CPR não encontrados.")

    smsresponse = sms.send_sms(phone_number={cpr_data.client_phone}, message={code.code[-4:]})

    if smsresponse is False:
        raise ResponseException.not_found("SMS não enviado.")

    return {"numero": cpr_data.client_phone}
