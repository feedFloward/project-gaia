import { classObject } from './cls'

export type clfObject = {
    text: string,
    value: string,
    specs?: Object<Array> // hier sowas wie type clfSpecsInterface = SvmSpecs | ...
}

interface ClfResponse {
    Z: number[]
}

interface TrainingSpecs {
    test_size: number
}

interface SvmSpecs {
    kernel: string[]
}

interface ModelSpecs {
    svmSpecs: SvmSpecs
}

// type

export interface ClfState {
    classes: classObject[],
    currentClass: classObject,
    classifiers: clfObject[],
    selectedClassifier: clfObject | undefined,
    inputspace : Object,
    modelSpecData: ModelSpecs,
    clfResponse: ClfResponse,
    trainingSpecs: TrainingSpecs
}