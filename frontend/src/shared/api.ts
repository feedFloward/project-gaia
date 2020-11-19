import Axios, * as axios from 'axios';
import {clfObject, classObject, TrainingSpecs} from '@/types/classification'

const baseUrl = "http://127.0.0.1:8000/api";
const version = "/v0.1";
const classification = "/classification";

const trainRequest = async function(data: classObject[], inputspace: Record<string, any>, model: clfObject, trainSpecs: TrainingSpecs) {
    Axios.defaults.xsrfCookieName = 'csrftoken';
    Axios.defaults.xsrfHeaderName = 'X-CSRFToken';

    console.log(JSON.stringify(
        {
            data: data,
            inputspace: inputspace,
            model: model,
            train_specs: trainSpecs // eslint-disable-line   
        }
    ))

    const response = await axios.default.post(baseUrl+version+classification, JSON.stringify(
        {
            data: data,
            inputspace: inputspace,
            model: model,
            train_specs: trainSpecs // eslint-disable-line
        }
    )).catch(error => {
        throw new Error(`GAIA api service ${error}`)
    })
    return response.data
};

export const data = {
    trainRequest,
};