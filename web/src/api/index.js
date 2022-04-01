import { get, post } from './request'

const HttpManager = {
    getScores: (params) => post('/', params)
}

export {HttpManager}